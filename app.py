from email.mime.multipart import MIMEMultipart

#
message = MIMEMultipart()

# E-mail Body
message['to'] = "samijiyemi2gmail.com"
message['from'] = "info@samijiyemi.co.uk"
message['subject'] = "Sending E-mail From Python"
