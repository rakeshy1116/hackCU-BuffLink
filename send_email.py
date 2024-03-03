from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Sender email
sender_email = 'arkleetcodef22@gmail.com'
# SMTP server configuration
smtp_server = 'smtp.gmail.com'
# TLS port
smtp_port = 587  

# Gmail App Password
smtp_username = sender_email
smtp_password = 'oxst rtnw rfkh gjnw'

def send_email_to_user(receiver_email, subject, body):

    # Email configuration
    receiver_email = receiver_email
    subject = subject
    body = body

    # Create a MIMEText object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body to the message
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    # Secure the connection
    server.starttls()  
    server.login(smtp_username, smtp_password)

    # Send the email
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)

    # Close the connection
    server.quit()


