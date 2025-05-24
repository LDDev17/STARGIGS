from database import db
from app.models.client import Client
from sqlalchemy.exc import SQLAlchemyError

class ServiceError(Exception):
    def __init__(self, message, status_code=500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

# Service function to register or update a client profile
def register_client(id, email, profile_data):
    client = Client.query.filter_by(cognito_id=id).first()

    if client:
        client.first_name = profile_data.get('first_name', client.first_name)
        client.last_name = profile_data.get('last_name', client.last_name)
        client.user_name = profile_data.get('user_name', client.user_name)
        client.phone = profile_data.get('phone', client.phone)
        client.city = profile_data.get('city', client.city)
    
    else:
        client = Client(
            cognito_id=id,
            email=email,
            first_name=profile_data["first_name"],
            last_name=profile_data["last_name"],
            user_name=profile_data["user_name"],
            phone=profile_data.get("phone"),
            city=profile_data.get("city")
        )
        db.session.add(client)
    try:    
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise ServiceError(f"Error registering client: {str(e)}")
    return client

# Service function for getting a client by Cognito ID
def get_client(id):
    return Client.query.filter_by(cognito_id=id).first()

# Service function for updating a client by Cognito ID
def update_client(id, data):
    client = get_client(id)
    
    if client:
        client.first_name = data.get('first_name', client.first_name)
        client.last_name = data.get('last_name', client.last_name)
        client.user_name = data.get('user_name', client.user_name)
        client.email = data.get('email', client.email)
        client.phone = data.get('phone', client.phone)
        client.city = data.get('city', client.city)
        
        try:
            db.session.commit()
            return client
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ServiceError(f"Error updating client: {str(e)}")
    else:
        return None

# Service function for deleting a client by Cognito ID
def delete_client(id):
    client = Client.query.filter_by(cognito_id=id).first()
    
    if client:
        try:
            db.session.delete(client)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ServiceError(f"Error deleting client: {str(e)}")
    return False

# Service function to get all clients
def get_all_clients():
    clients = Client.query.all()
    return clients