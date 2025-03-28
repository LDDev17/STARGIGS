from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from models.client import Client

bcrypt = Bcrypt()

def authenticate_client(email, password):

    client = Client.query.filter_by(email=email).first()

    if client and bcrypt.check_password_hash(client.password, password):

        access_token =create_access_token(identity=client.id)
        return access_token
    
    return None
