"""
scheduler.py — Automated CU Boulder calendar scraper

Runs on a configurable interval (default: every 6 hours) to fetch new events
from the CU Boulder calendar and upload them to the DynamoDB NewEvents table.

Usage:
    python scheduler.py

Environment variables (set in .env):
    SCRAPE_INTERVAL_HOURS   How often to scrape (default: 6)
"""

import os
import logging
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from parse_calendar import get_data_list
from aws_dynamo import upload_to_dynamo

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s  %(levelname)s  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)

INTERVAL_HOURS = int(os.environ.get('SCRAPE_INTERVAL_HOURS', 6))


def scrape_and_upload():
    """Fetch events from the CU Boulder calendar and persist them to DynamoDB."""
    logger.info("Scrape job started")
    try:
        data_list = get_data_list()
        if data_list:
            upload_to_dynamo(data_list)
            logger.info("Uploaded %d events to DynamoDB", len(data_list))
        else:
            logger.warning("No events returned from the calendar scraper")
    except Exception as e:
        logger.error("Scrape job failed: %s", e)


if __name__ == '__main__':
    logger.info(
        "Scheduler starting — will scrape every %d hour(s). "
        "First run in 10 seconds.",
        INTERVAL_HOURS,
    )

    scheduler = BlockingScheduler()

    # Run immediately ~10 seconds after start, then on the configured interval
    start_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
    scheduler.add_job(
        scrape_and_upload,
        trigger='interval',
        hours=INTERVAL_HOURS,
        next_run_time=start_time,
        id='calendar_scraper',
        name='CU Boulder calendar scraper',
    )

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler stopped")
