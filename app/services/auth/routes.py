from flask import Blueprint, jsonify
from app.services.auth.controllers import verify_token,register_user

auth_bp = Blueprint("auth_bp", __name__)

auth_bp.route("/verify", methods=["GET"])(verify_token)


