from flask import Blueprint, jsonify
from app.blueprints.auth.controllers import verify_token

auth_bp = Blueprint("auth_bp", __name__, strict_slashes=False)

auth_bp.route("/verify", methods=["GET"])(verify_token)


