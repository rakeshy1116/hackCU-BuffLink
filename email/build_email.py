import datetime

def build_calendar_content(calendar_events):

    html_body = "<h1>Upcoming Events</h1>"

    for event in calendar_events:

        start_date_time = datetime.strptime(event['start_datetime'], '%Y-%m-%dT%H:%M:%S%z')
        end_date_time = datetime.strptime(event['end_datetime'], '%Y-%m-%dT%H:%M:%S%z')

        event_details = f"""
        <p><strong>{event['title']}</strong><br>
        {event['description']}<br>
        {event['url']}<br>
        Start: {start_date_time.strftime('%Y-%m-%d %H:%M')}<br>
        End: {end_date_time.strftime('%Y-%m-%d %H:%M')}</p>
        """
        html_body += event_details

    ical_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//MyCal//App//EN\n"

    for event in calendar_events:
        ical_event = f"""BEGIN:VEVENT
            UID:{datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')}@example.com
            DTSTAMP:{datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')}
            DTSTART:{start_date_time.strftime('%Y%m%dT%H%M%SZ')}
            DTEND:{end_date_time.strftime('%Y%m%dT%H%M%SZ')}
            SUMMARY:{event['title']}
            DESCRIPTION:{event['description']}
            END:VEVENT
        """

        ical_content += ical_event

    ical_content += "END:VCALENDAR\n"

    return ical_content

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