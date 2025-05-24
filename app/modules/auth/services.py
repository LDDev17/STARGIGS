import jwt
import requests
from functools import wraps
from flask import request, jsonify, g
import json
import os

# AWS Cognito configuration loaded from environment variables
COGNITO_REGION = os.getenv("COGNITO_REGION")
USER_POOL_ID = os.getenv("USER_POOL_ID")
COGNITO_ISSUER = os.getenv("COGNITO_ISSUER")

# URL to fetch the JSON Web Key Set (JWKS) for token verification
JWKS_URL = f"{COGNITO_ISSUER}/.well-known/jwks.json"
JWKS = requests.get(JWKS_URL).json()["keys"]

def get_public_key(token):
    """
    Retrieves the public key from the JWKS that matches the 'kid' in the token header.
    """
    headers = jwt.get_unverified_header(token)
    kid = headers["kid"]

    key = next((k for k in JWKS if k["kid"] == kid), None)
    if not key:
        raise Exception("Public key not found in JWKS")
    
    return jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))

def verify_cognito_token(token):
    """
    Verifies and decodes a JWT token issued by AWS Cognito.
    Returns the decoded payload if valid, otherwise raises an exception.
    """
    public_key = get_public_key(token)
    payload = jwt.decode(
        token,
        public_key,
        algorithms=["RS256"],
        audience=os.getenv("COGNITO_CLIENT_ID"),
        issuer=COGNITO_ISSUER
    )
    return payload

def token_required(f):
    """
    Decorator to protect endpoints with JWT authentication.
    Validates the token and attaches the user info to Flask's 'g' context.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", None)

        if not auth_header:
            return jsonify({"message": "Token not found."}), 401
        
        try:
            token = auth_header.split(" ")[1]
            user = verify_cognito_token(token)
            g.user = user  # Store user info here
        except Exception:
            return jsonify({"message": "Token is invalid."}), 401
        
        return f(*args, **kwargs)
    return decorated