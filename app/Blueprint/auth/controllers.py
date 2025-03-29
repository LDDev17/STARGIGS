from flask import request, jsonify
from app.Blueprint.auth.services import authenticate_client


def login_client_controller():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    access_token = authenticate_client(email, password)

    if access_token:
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


