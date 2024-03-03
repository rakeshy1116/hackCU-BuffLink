from fetch_user_data import fetch_user_data_from_dynamo
from fetch_event_data import fetch_event_data_from_dynamo
from send_email import send_email_to_user
from build_email import build_email

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

            for event in events_list:
                
                try:
                    [subject, body] = build_email(user_data['userName'], event)
                    if subject is not None and body is not None:
                        send_email_to_user(user_data['emailId'], subject, body)
                except:
                    pass

#email_handler("yrakeshchowdary1116@gmail.com", ['4635410de53a7cb35da2807e440f1732c37bd5726977889f4ad6f49cfc342fa8aa9235c69f343c711268f6f6bbb762508a8ed7809c359ca03aad40fe6cb6b765'])








