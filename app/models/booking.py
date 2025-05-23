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
<<<<<<< HEAD
    
=======
    gig_ad=db.Column(db.String(50), nullable=False)
>>>>>>> b88c7a79fcad71aab134413d103c3957ae0d80c5

    client = db.relationship('Client', backref=db.backref('bookings', lazy=True))
    performer = db.relationship('Performer', backref=db.backref('bookings', lazy=True))
