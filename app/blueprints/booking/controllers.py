from flask import request, jsonify, g
from app.blueprints.auth.services import token_required
from app.blueprints.booking.services import (
    create_booking, update_booking, cancel_booking, check_performer_availability, get_booking_by_id
)
from app.models.schemas.booking_schema import booking_schema

# Create a new booking
@token_required
def create_new_booking():
    data = request.get_json()
    user_id = g.user['sub']

    booking = create_booking(user_id, data)

    if booking:
        return jsonify({"message": "Booking created successfully", "booking": booking_schema.dump(booking)}), 201
    return jsonify({"error": "Booking failed"}), 400

# Update an existing booking
@token_required
def update_existing_booking(booking_id):
    data = request.get_json()
    updated_booking = update_booking(booking_id, data)

    if updated_booking:
        return jsonify({"message": "Booking updated successfully", "booking": booking_schema.dump(updated_booking)}), 200
    return jsonify({"error": "Update failed"}), 400

# Cancel a booking
@token_required
def cancel_existing_booking(booking_id):
    result = cancel_booking(booking_id)

    if result:
        return jsonify({"message": "Booking canceled successfully"}), 200
    return jsonify({"error": "Cancellation failed"}), 400

# Check if a performer is available
def check_availability():
    performer_id = request.args.get("performer_id")

    if not performer_id:
        return jsonify({"message": "Performer not found."}, 400)
    
    booked_dates = check_performer_availability(performer_id)

    return jsonify({
        "performer_id": performer_id,
        "available": booked_dates
    }), 200


# Get a single booking by ID
@token_required
def get_booking(booking_id):
    booking = get_booking_by_id(booking_id)
    if booking:
        return jsonify({"booking": booking_schema.dump(booking)}), 200
    return jsonify({"error": "Booking not found"}), 404