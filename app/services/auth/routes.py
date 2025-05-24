from flask import Blueprint, jsonify
from app.services.auth.controllers import verify_token, register_user

# Blueprint for authentication-related routes
auth_bp = Blueprint("auth_bp", __name__)

# Route to verify the validity of a JWT token
auth_bp.route("/verify", methods=["GET"])(verify_token)