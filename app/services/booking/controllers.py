from flask import request, jsonify, g
from app.services.auth.services import token_required
from app.services.booking.services import (
    create_booking, update_booking, cancel_booking, check_performer_availability, get_booking_by_id, search_bookings
)
from app.models.schemas.booking_schema import booking_schema, bookings_schema
from app.models.client import Client
from app.models.performer import Performer

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
        return jsonify({"booking": booking}), 200
    else:
        return jsonify({"error": "Booking not found"}), 404

@token_required
def search_bookings_controller():
    user_sub = g.user["sub"]
    filters = request.args.to_dict()

    # Try to match sub to a Client
    client = Client.query.filter_by(cognito_id=user_sub).first()
    performer = Performer.query.filter_by(cognito_id=user_sub).first()

    user_type = None
    user_id = None

    if client:
        user_type = "client"
        user_id = client.id
    elif performer:
        user_type = "performer"
        user_id = performer.id
    else:
        return jsonify({"error": "User not found"}), 404

    results = search_bookings(user_id=user_id, role=user_type, filters=filters)

    return jsonify(bookings_schema.dump(results)), 200 

