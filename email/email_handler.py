from fetch_user_data import fetch_user_data_from_dynamo
from fetch_event_data import fetch_event_data_from_dynamo
from send_email import send_email_to_user
from build_email import build_event, build_calendar_content

def email_handler(user_email, hash_id_list):

    user_data = fetch_user_data_from_dynamo(user_email)

    if user_data is not None:

        previous_hash_ids = user_data['previousMails']
        new_hash_ids = []

        if previous_hash_ids is None:
            new_hash_ids = hash_id_list
        else:
            new_hash_ids = [id for id in hash_id_list if id not in previous_hash_ids]

        events_list = fetch_event_data_from_dynamo(new_hash_ids)

        if len(events_list) > 0:
            
            calendar_events = []
            email_content = None
            event_counter = 1

            for event in events_list:
                try:
                    calendar_events.append(build_event(event, event_counter))
                except:
                    pass
            
            email_content, html_body = build_calendar_content(calendar_events)
            
            if email_content is not None:
                send_email_to_user(user_data['emailId'], email_content, html_body)


# hash_ids = [
#     "4635410de53a7cb35da2807e440f1732c37bd5726977889f4ad6f49cfc342fa8aa9235c69f343c711268f6f6bbb762508a8ed7809c359ca03aad40fe6cb6b765",
#     "25f5594a165187faed50d4e4d4ea80cb1daff929b5c6b80bbcd1fde60babf59185894c0b68270becceebd53e031d7f2536470c63ada93ead90add209bdd9e9a1",
#     "1acf8611825d9275c5971626e1de6645b72dafa949f3bd48c1ddfaf212c6fcdecacd57ab03ffa9e994e13855a183ccf321bee564787dda8f0f970450d6225329",
# ]
# email_handler("krishnasandeep1825@gmail.com", hash_ids)



