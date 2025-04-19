from database import db
from app.models.booking import Booking
from datetime import datetime

# Create a new booking
def create_booking(user_id, data):
    try:
        new_booking = Booking(
            client_id=user_id,
            performer_id=data['performer_id'],
            event_date=datetime.strptime(data['event_date'], "%Y-%m-%d"),
            location=data['location'],
            price=data['price'],
            status="pending"
        )

        db.session.add(new_booking)
        db.session.commit()

        return new_booking.to_dict()
    except Exception as e:
        db.session.rollback()
        print("Error creating booking:", str(e))
        return None

# Update an existing booking
def update_booking(booking_id, data):
    booking = Booking.query.get(booking_id)
    
    if not booking:
        return None

    if 'event_date' in data:
        booking.event_date = datetime.strptime(data['event_date'], "%Y-%m-%d")
    if 'location' in data:
        booking.location = data['location']
    if 'price' in data:
        booking.price = data['price']
    if 'status' in data:
        booking.status = data['status']

    db.session.commit()
    return booking.to_dict()

# Cancel a booking
def cancel_booking(booking_id):
    booking = Booking.query.get(booking_id)

    if booking:
        booking.status = "canceled"
        db.session.commit()
        return True
    return False

# Check if performer is available
def check_performer_availability(performer_id):
    existing_booking = Booking.query.filter_by(performer_id=performer_id, status="confirmed").first()
    return existing_booking is None


# Get a booking by ID
def get_booking_by_id(booking_id):
    booking = Booking.query.get(booking_id)
    return booking.to_dict() if booking else None