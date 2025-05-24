
from flask_mail import Message
from app.extensions import mail
from flask import current_app

def send_booking_email(to, subject, body, html=None):
    msg = Message(
        subject=subject,
        recipients=[to],
        body=body,
        html=html
    )
    mail.send(msg)
