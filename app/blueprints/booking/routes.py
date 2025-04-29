from flask import Blueprint
from app.blueprints.booking.controllers import (
 create_new_booking,
    get_booking,
    update_existing_booking,
    cancel_existing_booking,
    check_availability
)

booking_blueprint = Blueprint('booking_bp', __name__)

booking_blueprint.route('/', methods=['POST'])(create_new_booking)  
booking_blueprint.route('/<int:id>/availability', methods=['GET'])(check_availability)  
booking_blueprint.route('/<int:id>', methods=['PUT'])(update_existing_booking)  
booking_blueprint.route('/<int:id>/cancel', methods=['DELETE'])(cancel_existing_booking)   
booking_blueprint.route('/<int:id>', methods=['GET'])(get_booking)