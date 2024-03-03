import datetime

def build_calendar_content(calendar_events):

    html_body = "<h1>Upcoming Events</h1>"

    for event in calendar_events:

        start_date_time = datetime.datetime.strptime(event['start_datetime'], '%Y-%m-%dT%H:%M:%S%z')
        end_date_time = datetime.datetime.strptime(event['end_datetime'], '%Y-%m-%dT%H:%M:%S%z')

        event_details = f"""
<p><strong>{event['title']}</strong><br><br>
{event['description']}<br><br>
{event['url']}<br><br>
Start: {start_date_time.strftime('%Y-%m-%d %H:%M')}<br>
End: {end_date_time.strftime('%Y-%m-%d %H:%M')}</p><br>
"""
        html_body += event_details

    ical_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Your Organization//Your App//EN\n"

    for event in calendar_events:

        start_date_time = datetime.datetime.strptime(event['start_datetime'], '%Y-%m-%dT%H:%M:%S%z')
        end_date_time = datetime.datetime.strptime(event['end_datetime'], '%Y-%m-%dT%H:%M:%S%z')

        ical_event = f"""BEGIN:VEVENT
UID:{datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')}@example.com
DTSTAMP:{datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')}
DTSTART:{start_date_time.strftime('%Y%m%dT%H%M%SZ')}
DTEND:{end_date_time.strftime('%Y%m%dT%H%M%SZ')}
SUMMARY:{event['title']}
END:VEVENT
"""

        ical_content += ical_event

    ical_content += "END:VCALENDAR\n"

    return ical_content, html_body

def build_event(event, event_counter):
    
    cur_event = {
        'summary': "Event " + str(event_counter),
        'title': event['title'],
        'description': event['description'],
        'url': event['url'],
        'start_datetime': event['startDate'],
        'end_datetime': event['endDate']
    }

    return cur_event

# body = build_email("Deveshwar", {'title': 'Connection', 'startDate': '2024-01-29T10:00:00-07:00', 'description': "Thanks", 'url': 'url'})
# print(body)