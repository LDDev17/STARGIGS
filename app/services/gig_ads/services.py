from database import db
from app.models.gig_ads import GigAd
from sqlalchemy.exc import SQLAlchemyError

def create_gig_ad(performer_id, data):
    """
    Creates a new gig advertisement for a performer.
    """
    try:
        gig_ad = GigAd(
            performer_id=performer_id,
            title=data["title"],
            description=data.get("description"),
            gig_type=data["gig_type"],
            location=data.get("location"),
            hourly_rate=data["hourly_rate"],
            media_url=data.get("media_url"),
            thumbnail_url=data.get("thumbnail_url"),
            availability=data.get("availability", {})
        )
        db.session.add(gig_ad)
        db.session.commit()
        return gig_ad
    except SQLAlchemyError as e:
        db.session.rollback()
        raise Exception(f"Error creating Gig Ad: {str(e)}")

def get_all_gig_ads():
    """
    Retrieves all gig advertisements from the database.
    """
    return GigAd.query.all()

def get_gig_ad(ad_id):
    """
    Retrieves a single gig advertisement by its unique ID.
    """
    return GigAd.query.get(ad_id)

def get_gig_ads_by_performer(performer_id):
    """
    Retrieves all gig advertisements posted by a specific performer.
    """
    return GigAd.query.filter_by(performer_id=performer_id).all()

def update_gig_ad(ad_id, data):
    """
    Updates an existing gig advertisement with new data.
    Returns the updated gig ad or None if not found.
    """
    gig_ad = GigAd.query.get(ad_id)
    if not gig_ad:
        return None

    gig_ad.title = data.get("title", gig_ad.title)
    gig_ad.description = data.get("description", gig_ad.description)
    gig_ad.gig_type = data.get("gig_type", gig_ad.gig_type)
    gig_ad.location = data.get("location", gig_ad.location)
    gig_ad.hourly_rate = data.get("hourly_rate", gig_ad.hourly_rate)
    gig_ad.media_url = data.get("media_url", gig_ad.media_url)
    gig_ad.thumbnail_url = data.get("thumbnail_url", gig_ad.thumbnail_url)
    gig_ad.availability = data.get("availability", gig_ad.availability)

    try:
        db.session.commit()
        return gig_ad
    except SQLAlchemyError as e:
        db.session.rollback()
        raise Exception(f"Error updating Gig Ad: {str(e)}")

def delete_gig_ad(ad_id):
    """
    Deletes a gig advertisement by its unique ID.
    Returns True if deletion was successful, False if not found.
    Raises an exception if a database error occurs.
    """
    gig_ad = GigAd.query.get(ad_id)
    if not gig_ad:
        return False

    try:
        db.session.delete(gig_ad)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        db.session.rollback()
        raise Exception(f"Error deleting Gig Ad: {str(e)}")