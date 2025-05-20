from flask import jsonify, request, g
from app.blueprints.auth.services import token_required

@token_required
def verify_token():
    return jsonify({"message": "Token is valid", "user": g.user}), 200