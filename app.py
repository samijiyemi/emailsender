from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

password = input("Enter your password: ")
print(password)

message = MIMEMultipart()

message['from'] = "Sam Ijiyemi"
message['to'] = "sam@eduboxglobal.org"
message['subject'] = "Congratulations!!!"
message.attach(MIMEText("Body Message from Sam"))

with smtplib.SMTP("smtp.gmail.com:587") as server:
    server.ehlo()
    server.starttls()
    server.login("sam@eduboxglobal.org", password=password)
    server.sendmail(message)
    server.quit()
    print("E-mail Sent!")
