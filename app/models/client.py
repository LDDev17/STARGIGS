from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy import Integer, String
from database import db

class Client(db.Model):
    """
    Client model represents a user who can book performers on the platform.
    Stores personal and contact information for each client.
    """
    __tablename__ = "Client"

    # Unique identifier for the client (Primary Key)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Client's first name
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)

    # Client's last name
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)

    # Username chosen by the client
    user_name: Mapped[str] = mapped_column(String(255), nullable=False)

    # Client's email address (must be unique)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    # Client's phone number (must be unique)
    phone: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)

    # City where the client resides
    city: Mapped[str] = mapped_column(String(100), nullable=False)

    # State where the client resides
    state: Mapped[str] = mapped_column(String(100), nullable=False)
    zip_code: Mapped[int] = mapped_column(Integer, nullable=False)
    profile_pic: Mapped[str] = mapped_column(String(500), nullable=True)
