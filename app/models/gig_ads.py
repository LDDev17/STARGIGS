from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, ForeignKey, Text, DateTime, JSON
from datetime import datetime
from database import db

class GigAd(db.Model):
    """
    GigAd model represents a gig advertisement posted by a performer.
    Stores details about the gig, including type, location, rates, and availability.
    """
    __tablename__ = "gig_ads"

    # Unique identifier for the gig advertisement (Primary Key)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Foreign key referencing the performer who posted the gig ad
    performer_id: Mapped[int] = mapped_column(ForeignKey("performers.id"), nullable=False)

    # Title of the gig advertisement
    title: Mapped[str] = mapped_column(String(255), nullable=False)

    # Detailed description of the gig
    description: Mapped[str] = mapped_column(Text)

    # Type/category of the gig
    gig_type: Mapped[str] = mapped_column(String(100), nullable=False)

    # Location where the gig will take place
    location: Mapped[str] = mapped_column(String(100))

    # Hourly rate for the gig
    hourly_rate: Mapped[float] = mapped_column(Float, nullable=False)
    
    # URL to media (image or video) associated with the gig ad
    media_url: Mapped[str] = mapped_column(String(500))         

    # URL to a thumbnail image for the gig ad
    thumbnail_url: Mapped[str] = mapped_column(String(500))     

    # Availability information (e.g., workdays, blocked days) stored as JSON
    availability: Mapped[dict] = mapped_column(JSON, default={})  

    # Timestamp when the gig ad was created
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Timestamp when the gig ad was last updated
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to the Performer model
    performer = relationship("Performer", back_populates="gig_ads")