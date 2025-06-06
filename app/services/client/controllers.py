from flask import request, jsonify, g
from app.services.client.services import register_client, get_client, update_client, delete_client
from app.models.schemas.client_schema import customer_schema, customers_schema
from app.services.auth.services import token_required

@token_required
def register_new_client():
    
    profile_data = request.get_json()
    user_info = g.user

    user = register_client(
        id = user_info["sub"],
        email = user_info["email"],
        profile_data=profile_data
    )

    return jsonify ({
        "message" : "User profile saved",
        "user": customer_schema.dump(user)
    }), 201

    
@token_required
def get_client_profile():
    client_id = request.user["sub"] # Get the client ID from the token (Cognito uses "sub" for user ID)
    client = get_client(client_id)

    if client:
        return jsonify(customer_schema.dump(client)), 200
    return jsonify({"message": "Client not found"}), 404


# Controller function for updating a client by ID
@token_required
def update_client_profile():
    client_id = request.user["sub"]  
    data = request.get_json()

    updated_client = update_client(client_id, data)

    if updated_client:
        return jsonify(customer_schema.dump(updated_client)), 200
    return jsonify({"message": "Client not found"}), 404


# Controller function for deleting a client by ID
@token_required
def delete_client_account():
    client_id = request.user["sub"]  

    result = delete_client(client_id)

    if result:
        return jsonify({"message": "Client account deleted successfully"}), 200
    return jsonify({"message": "Client not found"}), 404



