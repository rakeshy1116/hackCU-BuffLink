import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime

# Sender email
sender_email = 'arkleetcodef22@gmail.com'
# SMTP server configuration
smtp_server = 'smtp.gmail.com'
# TLS port
smtp_port = 587  

# Gmail App Password
smtp_username = sender_email
smtp_password = 'oxst rtnw rfkh gjnw'


def send_email_to_user(receiver_email, subject, ical_content):

    # Email configuration
    html_body = "<h1>Upcoming Events</h1>"

    msg = MIMEMultipart('mixed')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the HTML body
    msg.attach(MIMEText(html_body, 'html'))

    # Attach the iCalendar events
    part = MIMEBase('text', "calendar", method="REQUEST", name="events.ics")
    part.set_payload(ical_content)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="events.ics"')

    msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Successfully sent the email with multiple calendar invites!")
    except Exception as e:
        print(f"Failed to send email: {e}")