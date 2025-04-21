import jwt
import requests
from functools import wraps
from flask import request, jsonify, g
import json


COGNITO_REGION = ''
USER_POOL_ID = ''
COGNITO_ISSUER = '' 

JWKS_URL = f"{COGNITO_ISSUER}/.well-known/jwks.json"
JWKS = requests.get(JWKS_URL).json()["keys"]

def get_public_key(token):
    headers = jwt.get_unverified_header(token)
    kid = headers["kid"]

    key = next((k for k in JWKS if k["kid"] == kid), None)
    if not key:
        raise Exception("Public key not found in JWKS")
    
    return jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))

def verify_cognito_token(token):
    public_key = get_public_key(token)
    payload = jwt.decode(
        token,
        public_key,
        algorithms=["RS256"],
        audience= "client_id",
        issuer=COGNITO_ISSUER
    )
    return payload

def token_required(f):
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