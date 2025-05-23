<<<<<<< HEAD
=======
from app.models.performer import Performer
from app.models.client import Client
>>>>>>> b88c7a79fcad71aab134413d103c3957ae0d80c5
from database import db
from app.models.booking import Booking
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
<<<<<<< HEAD
=======
from app.utils.email import send_booking_email
>>>>>>> b88c7a79fcad71aab134413d103c3957ae0d80c5

# Create a new booking
def create_booking(user_id, data):
    try:
<<<<<<< HEAD
        new_booking = Booking(
            client_id=user_id,
            performer_id=data['performer_id'],
=======
        #Fetching performer info
        performer = Performer.query.get(data['performer_id'])
        if not performer:
            raise ValueError("Performer not found")

        # Fetching client info
        user = Client.query.get(user_id)
        if not user:
            raise ValueError("User not found")

        # Creating booking instance
        new_booking = Booking(
            client_id=user.id,
            performer_id=performer.id,
>>>>>>> b88c7a79fcad71aab134413d103c3957ae0d80c5
            event_date=datetime.strptime(data['event_date'], "%Y-%m-%d"),
            location=data['location'],
            price=data['price'],
            status="pending"
        )

        db.session.add(new_booking)
        db.session.commit()

<<<<<<< HEAD
        return new_booking
    except (SQLAlchemyError, ValueError) as e:
=======
        #Emailing Client
        client_subject = "Stargigs Booking Received 🎉"
        client_body = (
            f"Hi {user.name},\n\n"
            f"Your booking for {performer.name} on {new_booking.event_date.strftime('%B %d, %Y')} "
            f"at {new_booking.location} has been received. We'll confirm soon!"
        )
        send_booking_email(user.email, client_subject, client_body)

       #Emailing Performer
        performer_subject = "🎤 New Booking Request on Stargigs"
        performer_body = (
            f"Hi {performer.name},\n\n"
            f"You've received a new booking request from {user.name} "
            f"for {new_booking.event_date.strftime('%B %d, %Y')} at {new_booking.location}."
        )
        send_booking_email(performer.email, performer_subject, performer_body)

        return new_booking.to_dict()

    except Exception as e:
>>>>>>> b88c7a79fcad71aab134413d103c3957ae0d80c5
        db.session.rollback()
        raise Exception("Error creating booking:", str(e))
        

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
    return booking

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
    existing_bookings = Booking.query.filter_by(
        performer_id=performer_id, 
        status="confirmed"
        ).all()
    booked_dates = [booking.event_date.strftime('%Y-%M-%d') for booking in existing_bookings]
    return booked_dates


# Get a booking by ID
def get_booking_by_id(booking_id):
    booking = Booking.query.get(booking_id)
<<<<<<< HEAD
    return booking.to_dict() if booking else None
=======
    return booking.to_dict() if booking else None




def confirm_booking(booking, user_email, performer_email):
    subject = "Your Stargigs Booking Confirmation 🎤"
    body = f"Thanks for booking {booking.performer_name} on {booking.date}!"

#     # Send confirmation email to user
    send_booking_email(user_email, subject, body)
#     # Send confirmation email to performer
    send_booking_email(performer_email, f"New Booking from {booking.user_name}", body)

def search_bookings(user_id, role, filters):
    query = Booking.query

    # Filter by user type
    if role == "client":
        query = query.filter_by(client_id=user_id)
    elif role == "performer":
        query = query.filter_by(performer_id=user_id)

    # Optional filters
    if "status" in filters:
        query = query.filter(Booking.status == filters["status"])

    if "start_date" in filters:
        query = query.filter(Booking.event_date >= filters["start_date"])

    if "end_date" in filters:
        query = query.filter(Booking.event_date <= filters["end_date"])

    return query.order_by(Booking.event_date.desc()).all()
>>>>>>> b88c7a79fcad71aab134413d103c3957ae0d80c5
