from flask import jsonify, request, g
from app.modules.auth.services import token_required

# Endpoint to verify the validity of a JWT token.
@token_required
def verify_token():
    return jsonify({"message": "Token is valid", "user": g.user}), 200