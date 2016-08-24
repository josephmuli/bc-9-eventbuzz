import os
import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMETEXT import MIMETEXT
from email import Encoders


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'eventbuzzer@gmail.com'
DEFAULT_FROM_EMAIL = 'eventbuzzer@gmail.com'
EMAIL_HOST_PASSWORD = 'Shellshocked'


# attachment is a ticket(ticket data, i.e ticket no, with event details)
def mail(to, subject, text, attach):
	msg = MIMEMultipart()
	msg['From'] = EMAIL_HOST_USER
	msg['To'] = to
	msg['Subject'] = subject
	msg.attach(MIMETEXT(text))