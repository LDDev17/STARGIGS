from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.Blueprint.booking.services import (
    create_booking, update_booking, cancel_booking, check_performer_availability, get_booking_by_id
)

# Create a new booking
@jwt_required()
def create_new_booking():
    data = request.get_json()
    user_id = get_jwt_identity()

    booking = create_booking(user_id, data)

    if booking:
        return jsonify({"message": "Booking created successfully", "booking": booking}), 201
    return jsonify({"error": "Booking failed"}), 400

# Update an existing booking
@jwt_required()
def update_existing_booking(booking_id):
    data = request.get_json()
    updated_booking = update_booking(booking_id, data)

    if updated_booking:
        return jsonify({"message": "Booking updated successfully", "booking": updated_booking}), 200
    return jsonify({"error": "Update failed"}), 400

# Cancel a booking
@jwt_required()
def cancel_existing_booking(booking_id):
    result = cancel_booking(booking_id)

    if result:
        return jsonify({"message": "Booking canceled successfully"}), 200
    return jsonify({"error": "Cancellation failed"}), 400

# Check if a performer is available
def check_availability():
    performer_id = request.args.get("performer_id")
    available = check_performer_availability(performer_id)
    return jsonify({"performer_id": performer_id, "available": available}), 200


# Get a single booking by ID
@jwt_required()
def get_booking(booking_id):
    booking = get_booking_by_id(booking_id)
    if booking:
        return jsonify({"booking": booking}), 200
    return jsonify({"error": "Booking not found"}), 404