from database import db
from app.models.client import Client


def register_client(id, email, profile_data):
    client = Client.query.filter_by(cognito_id=id).first()

    if client:
        client.first_name = profile_data.get("first_name", client.first_name)
        client.last_name = profile_data.get("last_name", client.last_name)
        client.user_name = profile_data.get("user_name", client.user_name)
        client.phone = profile_data.get("phone", client.phone)
        client.city = profile_data.get("city", client.city)
    
    else:
        client = Client(
            id=id,
            email=email,
            first_name=profile_data["first_name"],
            last_name=profile_data["last_name"],
            user_name=profile_data["user_name"],
            phone=profile_data.get("phone"),
            city=profile_data.get("city")
        )
        db.session.add(client)
    db.session.commit()
    
    return client

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

