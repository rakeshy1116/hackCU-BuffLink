import datetime

def build_calendar_content(calendar_events):

    for event in calendar_events:
        event_details = f"""
        <p><strong>{event['title']}</strong><br>
        {event['description']}<br>
        {event['url']}<br>
        Start: {event['start_datetime'].strftime('%Y-%m-%d %H:%M')}<br>
        End: {event['end_datetime'].strftime('%Y-%m-%d %H:%M')}</p>
        """
        html_body += event_details

    ical_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//MyCal//App//EN\n"

    for event in calendar_events:
        ical_event = f"""BEGIN:VEVENT
            UID:{datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')}@example.com
            DTSTAMP:{datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')}
            DTSTART:{event['start_datetime'].strftime('%Y%m%dT%H%M%SZ')}
            DTEND:{event['end_datetime'].strftime('%Y%m%dT%H%M%SZ')}
            SUMMARY:{event['title']}
            DESCRIPTION:{event['description']}
            END:VEVENT
        """

        ical_content += ical_event

    ical_content += "END:VCALENDAR\n"

    return ical_content

def build_event(event, event_counter):
    
    cur_event = {
        'summary': "Event " + event_counter,
        'title': event['title'],
        'description': event['description'],
        'url': event['url'],
        'start_datetime': event['startDate'],
        'end_datetime': event['endDate']
    }

    return cur_event

# body = build_email("Deveshwar", {'title': 'Connection', 'startDate': '2024-01-29T10:00:00-07:00', 'description': "Thanks", 'url': 'url'})
# print(body)