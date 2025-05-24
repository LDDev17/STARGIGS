from database import db
from app.models.performer import Performer

# Update the fields of a Performer instance with provided data
def update_performer(performer, data):
    performer.first_name = data.get('first_name', performer.first_name)
    performer.last_name = data.get('last_name', performer.last_name)
    performer.user_name = data.get('user_name', performer.user_name)
    performer.email = data.get('email', performer.email)
    performer.phone = data.get('phone', performer.phone)
    performer.city = data.get('city', performer.city)

# Create a new performer profile or update an existing one based on Cognito user ID
def create_or_update_performer_profile(id, email, profile_data):
    performer = Performer.query.filter_by(cognito_id=id).first()

    if performer:
        update_performer(performer, profile_data)
    else:
        performer = Performer(
            cognito_id=id,
            email=email,
            first_name=profile_data["first_name"],
            last_name=profile_data["last_name"],
            user_name=profile_data["user_name"],
            phone=profile_data.get("phone"),
            city=profile_data.get("city")
        )
        db.session.add(performer)
    db.session.commit()
    return performer

# Retrieve a performer by Cognito user ID
def get_performer(id):
    return Performer.query.filter_by(cognito_id=id).first()    

# Delete a performer profile by Cognito user ID
def delete_performer(id):
    performer = Performer.query.filter_by(cognito_id=id).first()

    if performer:
        try:
            db.session.delete(performer)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error deleting performer: {str(e)}")
    return False

# Retrieve all performers with pagination
def get_all_performers(page=1, per_page=10):
    pagination = Performer.query.paginate(page=page, per_page=per_page, error_out=False)
    return pagination.items