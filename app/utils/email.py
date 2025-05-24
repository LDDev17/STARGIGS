from flask_mail import Message
from app.extensions import mail
from flask import current_app

# Utility function to send a booking-related email
def send_booking_email(to, subject, body, html=None):
    # Create a new email message with the given subject, recipient, and body
    msg = Message(
        subject=subject,
        recipients=[to],
        body=body,
        html=html
    )
    # Send the email using Flask-Mail
    mail.send(msg)