from app.utils.email import send_booking_email

# Test function to verify email sending functionality
def test_email_sending(mail):
    # Use Flask-Mail's record_messages context to capture outgoing emails
    with mail.record_messages() as outbox:
        send_booking_email("test@example.com", "Subject", "Body text")
        # Assert that one email was sent
        assert len(outbox) == 1
        # Assert that the subject of the sent email matches
        assert outbox[0].subject == "Subject"