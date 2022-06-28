from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

password = input("what is your password: ")
print(password)

message = MIMEMultipart()

message['from'] = "Sam Ijiyemi"
message['to'] = "sam@eduboxglobal.org"
message['subject'] = "Congratulations!!!"
message.attach(MIMEText("Body Message from Sam"))

with smtplib.SMTP_SSL("smtp.gmail.com") as server:
    server.ehlo()
    server.starttls()
    server.login("sam@eduboxglobal.org", password=password)
    server.send_message(message)
    print("E-mail Sent!")
