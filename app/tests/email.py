from app.utils.email import send_booking_email


def test_email_sending(mail):
    with mail.record_messages() as outbox:
        send_booking_email("test@example.com", "Subject", "Body text")
        assert len(outbox) == 1
        assert outbox[0].subject == "Subject"
