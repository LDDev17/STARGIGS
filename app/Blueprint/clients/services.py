from database import db
from models.client import Client
from werkzeug.security import generate_password_hash

def register_client(data):
    existing_client = Client.query.filter_by(email=data['email']).first()
    
    if existing_client:
        return None  # Client already exists

    hashed_password = generate_password_hash(data['password'])

    # Create and add new client
    new_client = Client(
        first_name=data['first_name'],
        last_name=data['last_name'],
        user_name=data['username'],
        email=data['email'],
        phone=data['phone'],
        city=data['city'],
        password=hashed_password
    )
    
    db.session.add(new_client)
    db.session.commit()
    
    return new_client

# Service function for getting a client by ID
def get_client(id):
    return Client.query.get(id)

# Service function for updating a client by ID
def update_client(id, data):
    client = Client.query.get(id)
    
    if client:
        client.first_name = data.get('first_name', client.first_name)
        client.last_name = data.get('last_name', client.last_name)
        client.user_name = data.get('username', client.user_name)
        client.email = data.get('email', client.email)
        client.phone = data.get('phone', client.phone)
        client.city = data.get('city', client.city)
        
        # Only update the password if provided
        if 'password' in data:
            client.password = generate_password_hash(data['password'])
        
        try:
            db.session.commit()
            return client
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error updating client: {str(e)}")
    else:
        return None

# Service function for deleting a client by ID
def delete_client(id):
    client = Client.query.get(id)
    
    if client:
        try:
            db.session.delete(client)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error deleting client: {str(e)}")
    return False

# Service function to get all clients
def get_all_clients():
    return Client.query.all()