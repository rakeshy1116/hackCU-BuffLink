from fetch_user_data import fetch_user_data_from_dynamo
from fetch_event_data import fetch_event_data_from_dynamo
from send_email import send_email_to_user
from user_dynamo import *
from build_email import build_event, build_calendar_content

def email_handler(user_email, hash_id_list):
    user_data = get_user_data(user_email)

    if user_data is not None:
        previous_mails = user_data.get('previousMails').get('L', [])
        previous_mails_list = [item.get('S') for item in previous_mails]
        new_hash_ids = []
        print("previous_mails")
        print(previous_mails_list)
        print("previous_hash_ids")
        print(previous_mails_list)
        if previous_mails_list is None:
            new_hash_ids = hash_id_list
            # print("new_hash_ids")
            # print(new_hash_ids)
            put_user_data(user_data['userName'].get('S'), user_data['emailId'].get('S'), hash_id_list, user_data['extensionPrompts'].get('L', []))
        else:
            new_hash_ids = [id for id in hash_id_list if id not in previous_mails_list]
            for x in new_hash_ids:
                previous_mails_list.append(x)
            put_user_data(user_data['userName'].get('S'), user_data['emailId'].get('S'), previous_mails_list, user_data['extensionPrompts'].get('L',[]))
            # print("previous_hash_ids+new_hash_ids")
            # print(previous_hash_ids+new_hash_ids)

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
                send_email_to_user(user_data['emailId'].get('S'), email_content, html_body)

#email_handler("yrakeshchowdary1116@gmail.com", ['4635410de53a7cb35da2807e440f1732c37bd5726977889f4ad6f49cfc342fa8aa9235c69f343c711268f6f6bbb762508a8ed7809c359ca03aad40fe6cb6b765'])








