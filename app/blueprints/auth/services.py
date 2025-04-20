import jwt
import requests
from functools import wraps
from flask import request, jsonify
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
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"message": "Token not found."}), 401
        
        try:
            user = verify_cognito_token(token)
            request.user = user
        except Exception as e:
            return jsonify({"message": f"Token is invalid:{str(e)}"}), 401
        
        return f(*args, **kwargs)
    return decorated