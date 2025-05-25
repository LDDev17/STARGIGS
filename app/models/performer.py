from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from database import db

class Performer(db.Model):
    __tablename__ = "Performer"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    user_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    phone: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str] = mapped_column(String(100), nullable=False)
    zip_code: Mapped[int] = mapped_column(Integer, nullable=False)
    profile_pic: Mapped[str] = mapped_column(String(500), nullable=True)

    # Relationship to the GigAd model (one performer can have many gig ads)
    gig_ads = relationship("GigAd", back_populates="performer", cascade="all, delete-orphan")