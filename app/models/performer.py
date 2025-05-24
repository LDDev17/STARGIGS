from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from database import db

class Performer(db.Model):
    """
    Performer model represents a user who can post gig advertisements and be booked by clients.
    Stores personal and contact information for each performer.
    """
    __tablename__ = "user"

    # Unique identifier for the performer (Primary Key)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Performer's first name
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)

    # Performer's last name
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)

    # Username chosen by the performer
    user_name: Mapped[str] = mapped_column(String(255), nullable=False)

    # Performer's email address (must be unique)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    # Performer's phone number (must be unique)
    phone: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)

    # City where the performer resides
    city: Mapped[str] = mapped_column(String(100), nullable=False)

    # State where the performer resides
    state: Mapped[str] = mapped_column(String(100), nullable=False)

    # Zip code of the performer's address
    zip_code: Mapped[int] = mapped_column(Integer, nullable=False)

    # URL or path to the performer's profile picture
    profile_pic:  Mapped[str] = mapped_column(String(500))

    # Relationship to the GigAd model (one performer can have many gig ads)
    gig_ads = relationship("GigAd", back_populates="performer", cascade="all, delete-orphan")