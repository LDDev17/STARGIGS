from sqlalchemy.orm import  Mapped, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey

from app import db

class Booking(db.Model):
    """
    Booking model represents a booking record between a client and a performer.
    """
    __tablename__ = "booking"
    
    # Primary key for the booking record
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign key referencing the client who made the booking
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    
    # Foreign key referencing the performer who is booked
    performer_id = db.Column(db.Integer, db.ForeignKey('performer.id'), nullable=False)
    
    # Date and time when the booking is scheduled
    booking_date = db.Column(db.DateTime, nullable=False)
    
    # Status of the booking (e.g., pending, confirmed, cancelled)
    status = db.Column(db.String(50), nullable=False)
    
    # Reference to the gig advertisement associated with the booking
    gig_ad = db.Column(db.String(50), nullable=False)

    # Relationship to the Client model
    client = db.relationship('Client', backref=db.backref('bookings', lazy=True))
    
    # Relationship to the Performer model
    performer = db.relationship('Performer', backref=db.backref('bookings', lazy=True))