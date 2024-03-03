import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = 'arkleetcodef22@gmail.com'
receiver_email = 'yrakeshchowdary1116@gmail.com'
subject = 'Test Email'
body = 'This is a test email sent from Python using Gmail App Passwords.'

# Create a MIMEText object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the body to the message
message.attach(MIMEText(body, 'plain'))

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # TLS port

# Gmail App Password
smtp_username = sender_email
smtp_password = 'oxst rtnw rfkh gjnw'

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Secure the connection
server.login(smtp_username, smtp_password)

# Send the email
text = message.as_string()
server.sendmail(sender_email, receiver_email, text)

# Close the connection
server.quit()

print('Email sent successfully.')
