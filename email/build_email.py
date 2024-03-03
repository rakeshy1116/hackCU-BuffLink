
def build_email(user_name, event):
    
    subject = None
    body = None

    if user_name is not None and event is not None:

        subject = event['title'] + " event on " + event['startDate'][:10]
        body = "Hi " + user_name + "," + " here\'s your personalized event,\n\n" + event['description'] + "\n\nEvent url:" + event['url']+ "\n\nThanks,\nTeam"

    return [subject, body]

# [subject, body] = build_email("Deveshwar", {'title': 'Connection', 'startDate': '2024-01-29T10:00:00-07:00', 'description': "Thanks"})
# print(body)