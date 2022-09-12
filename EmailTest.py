import smtplib, ssl
import settings

def sendErrorEmail(message):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(settings.sender_email, settings.emailPassword)
        server.sendmail(settings.sender_email, settings.receiver_email, message)

print("Hello")
inputMessage = input("type your message and press enter: ")
message = f"""\
Subject: Hi there
{inputMessage}
This message is sent from Python."""
sendErrorEmail(message)

print("Complete.")