from sqlalchemy.orm import  Mapped, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey

from app import db

class Booking(db.Model):
    __tablename__ = "booking"
    
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    performer_id = db.Column(db.Integer, db.ForeignKey('performer.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    gig_ad=db.Column(db.String(50), nullable=False)

    client = db.relationship('Client', backref=db.backref('bookings', lazy=True))
    performer = db.relationship('Performer', backref=db.backref('bookings', lazy=True))
