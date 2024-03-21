import email
from multiprocessing import context


email_sender = "nguyenquocthai7803@gmail.com"
email_password = "0328774884Thai"
import ssl
import smtplib
from email.message import EmailMessage

email_receiver = email_sender
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = "Test Subject"
em.set_content("Hello, I am Test Body")

context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls(context=context)
    smtp.login(email_sender, email_password)
    smtp.send_message(em)