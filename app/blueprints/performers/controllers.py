from flask import request, jsonify, g
from app.blueprints.performers.services import get_all_performers, delete_performer, get_performer, update_performer, create_or_update_performer_profile
from app.models.schemas.performer_schema import performer_schema, performers_schema
from app.blueprints.auth.services import token_required

@token_required
def complete_performer_profile():
    profile_data = request.get_json()
    user_info = g.user

    try:
        performer = create_or_update_performer_profile(
            id = user_info["sub"],
            email = user_info["email"],
            profile_data=profile_data
        )

        return jsonify ({
            "message" : "Performer profile saved",
            "performer": performer_schema.dump(performer)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

    try:
        updated_performer = update_performer(performer_id, data)

        if updated_performer:
            return jsonify({
                "message": "Profile updated successfully",
                "performer": performer_schema.dump(updated_performer)}), 200
        
        return jsonify({"message": "Performer not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@token_required
def delete_my_performer_profile():
    performer_id = request.user["sub"]
    success = delete_performer(performer_id)
    try:
        if success:
            return jsonify ({"message": "Profile deleted"}), 200
        
        return jsonify({"message": "Performer not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
def get_all():
    performers = get_all_performers()
    return jsonify(performers_schema.dump(performers)), 200