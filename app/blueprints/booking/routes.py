from flask import Blueprint
from app.blueprints.booking.controllers import (
 create_new_booking,
    get_booking,
    update_existing_booking,
    cancel_existing_booking,
<<<<<<< HEAD
    check_availability
=======
    check_availability,
    search_bookings_controller
>>>>>>> b88c7a79fcad71aab134413d103c3957ae0d80c5
)

booking_blueprint = Blueprint('booking_bp', __name__)

booking_blueprint.route('/', methods=['POST'])(create_new_booking)  
booking_blueprint.route('/availability', methods=['GET'])(check_availability)  
booking_blueprint.route('/<int:id>', methods=['GET'])(get_booking)
booking_blueprint.route('/<int:id>', methods=['PUT'])(update_existing_booking)  
booking_blueprint.route('/<int:id>/cancel', methods=['DELETE'])(cancel_existing_booking)   
<<<<<<< HEAD
=======
booking_blueprint.route('/search', methods=['GET'])(search_bookings_controller)
>>>>>>> b88c7a79fcad71aab134413d103c3957ae0d80c5
