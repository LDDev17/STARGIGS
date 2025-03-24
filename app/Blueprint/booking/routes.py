from flask import Blueprint
#from booking.controllers import create_booking, get_booking, update_booking, delete_booking, get_all_bookings


booking_blueprint = Blueprint('booking_bp', __name__)

booking_blueprint.route('/', methods=['POST'])#(create_booking)  
booking_blueprint.route('/<int:id>', methods=['GET'])#(get_booking)  
booking_blueprint.route('/<int:id>', methods=['PUT'])#(update_booking)  
booking_blueprint.route('/<int:id>', methods=['DELETE'])#(delete_booking)  
booking_blueprint.route('/', methods=['GET'])#(get_all_bookings)