import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 465
password = input("Please enter your password")
context = ssl.create_default_context()
sender_email = "nsitlani03@gmail.com"
receiver_email = "sitlani.namrata@yahoo.in"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
        Hi, this is the plain text"""
html = """\
    <html>
        <body>
            This text comes from html
        </body>
    </html>
    """
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:

    server.login("nsitlani03@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message.as_string())

