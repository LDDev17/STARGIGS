from flask import Blueprint
from app.modules.booking.controllers import (
    create_new_booking,
    get_booking,
    update_existing_booking,
    cancel_existing_booking,
    check_availability,
    search_bookings_controller
)

booking_blueprint = Blueprint('booking_bp', __name__)

# Route to create a new booking
booking_blueprint.route('/', methods=['POST'])(create_new_booking)  

# Route to check performer availability
booking_blueprint.route('/availability', methods=['GET'])(check_availability)  

# Route to get a booking by ID
booking_blueprint.route('/<int:id>', methods=['GET'])(get_booking)

# Route to update an existing booking
booking_blueprint.route('/<int:id>', methods=['PUT'])(update_existing_booking)  

# Route to cancel a booking
booking_blueprint.route('/<int:id>/cancel', methods=['DELETE'])(cancel_existing_booking)   

# Route to search bookings
booking_blueprint.route('/search', methods=['GET'])(search_bookings_controller)