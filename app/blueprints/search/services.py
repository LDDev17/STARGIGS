from app.models.performer import Performer


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
    
    performers = query.all()

    return performers