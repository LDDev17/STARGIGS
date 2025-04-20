from database import db
from app.models.performer import Performer

def create_or_update_performer_profile(id, email, profile_data):
    performer = Performer.query.filter_by(id=id).first()

    if performer:
        performer.first_name = profile_data.get("first_name", performer.first_name)
        performer.last_name = profile_data.get("last_name", performer.last_name)
        performer.user_name = profile_data.get("user_name", performer.user_name)
        performer.phone = profile_data.get("phone", performer.phone)
        performer.city = profile_data.get("city", performer.city)
    
    else:
        performer = Performer(
            id=id,
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

def get_performer(id):
    return Performer.query.get(id)


def update_performer(id, data):
    performer = Performer.query.get(id)

    if performer :
        performer.first_name = data.get('first_name', performer.first_name)
        performer.last_name = data.get('last_name', performer.last_name)
        performer.user_name = data.get('user_name', performer.user_name)
        performer.email = data.get('email', performer.email)
        performer.phone = data.get('phone', performer.phone)
        performer.city = data.get('city', performer.city)
        

        try:
            db.session.commit()
            return performer
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error updating performer: {str(e)}")
    
    return None

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

def get_all_performers():
    return Performer.query.all()