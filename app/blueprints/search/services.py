from app.models.performer import Performer
from database import db
from app.models.booking import Booking
from datetime import datetime

def search_performers_services(filters):
    query = Performer.query

    # Apply filters conditionally if provided
    if filters.get('name'):  # Check if the 'name' filter is present
        query = query.filter(Performer.name.ilike(f"%{filters['name']}%"))
    
    if filters.get('price'):  # Check if the 'price' filter is present
        try:
            query = query.filter(Performer.price <= float(filters['price']))
        except ValueError:
            pass  # Handle invalid price input gracefully
    
    if filters.get('location'):  # Check if the 'location' filter is present
        query = query.filter(Performer.city.ilike(f"%{filters['location']}%"))
    
    if filters.get('ratings'):  # Check if the 'ratings' filter is present
        try:
            query = query.filter(Performer.rating >= float(filters['ratings']))
        except ValueError:
            pass  # Handle invalid ratings input gracefully
    
    if filters.get('event_date'):
        try:
            event_date = datetime.strptime(filters["event_date"], "%Y-%m-%d")

            booked_ids = db.session.query(Booking.performer_id).filter(
                Booking.event_date == event_date,
                Booking.status == "confirmed"
            ).subquery()

            query = query.filter(~Performer.id.in_(booked_ids))
        
        except ValueError:
            pass
    
    performers = query.all()

    return performers