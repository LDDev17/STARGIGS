from flask import request, jsonify
from app.blueprints.client.services import register_client, get_client, update_client, delete_client, get_all_clients
from app.models.schemas.client_schema import customer_schema, customers_schema
from app.blueprints.auth.services import token_required


def register_new_client():
    data = request.get_json()

    # Register the client using the service
    client = register_client(data)

    if client:
        return jsonify({'message': 'Client registered successfully!'}), 201
    return jsonify({'message': 'Client already exists'}), 400
    
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



