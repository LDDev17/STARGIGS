from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, ForeignKey, Text, DateTime, JSON
from datetime import datetime
from database import db

class GigAd(db.Model):
    __tablename__ = "gig_ads"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    performer_id: Mapped[int] = mapped_column(ForeignKey("performers.id"), nullable=False)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    gig_type: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(100))
    hourly_rate: Mapped[float] = mapped_column(Float, nullable=False)
    
    media_url: Mapped[str] = mapped_column(String(500))         # For image or video
    thumbnail_url: Mapped[str] = mapped_column(String(500))     # Separate thumbnail

    availability: Mapped[dict] = mapped_column(JSON, default={})  # Workdays/blocked days

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    performer = relationship("Performer", back_populates="gig_ads")