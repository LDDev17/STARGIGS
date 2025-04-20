from flask import request, jsonify
from app.blueprints.performers.services import get_all_performers, delete_performer, get_performer, update_performer, create_or_update_performer_profile
from app.models.schemas.performer_schema import performer_schema, performers_schema
from app.blueprints.auth.services import token_required

@token_required
def complete_performer_profile():
    profile_data = request.get_json()
    user_info = request.user

    performer = create_or_update_performer_profile(
        id = user_info["sub"],
        email = user_info["sub"],
        profile_data=profile_data
    )

    return jsonify ({
        "message" : "Performer profile saved",
        "performer": performer_schema.dump(performer)
    })


@token_required
def get_performer_profile():
    performer_id = request.user["sub"] # Cognito user ID
    performer = get_performer(performer_id)

    if performer:
        return jsonify(performer_schema.dump(performer)), 200
    
    return jsonify({"message": "Performer not found"}), 404

@token_required
def update_performer_profile():
    performer_id = request.user["sub"]
    data=request.get_json()

    updated_performer = update_performer(performer_id, data)

    if updated_performer:
        return jsonify({
            "message": "Profile updated successfully",
            "performer": performer_schema.dump(updated_performer)}), 200
    
    return jsonify({"message": "Performer not found"}), 404

@token_required
def delete_my_performer_profile():
    user_info = request.user["sub"]
    success = delete_performer(user_info)

    if success:
        return jsonify ({"message": "Profile deleted"}), 200
    
    return jsonify({"message": "Performer not found"}), 404

def get_all():
    performers = get_all_performers()
    return jsonify(performers_schema(performers)), 200