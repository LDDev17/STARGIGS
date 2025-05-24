from flask import Blueprint, jsonify
from app.modules.auth.controllers import verify_token

# Blueprint for authentication-related routes
auth_bp = Blueprint("auth_bp", __name__)

# Route to verify the validity of a JWT token
auth_bp.route("/verify", methods=["GET"])(verify_token)