from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, ForeignKey, DateTime, func

db = SQLAlchemy()

class Payment(db.Model):
    """
    Payment model represents a payment transaction made by a client.
    Stores payment details including amount, status, method, and timestamp.
    """
    __tablename__ = "payments"

    # Unique identifier for the payment (Primary Key)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Foreign key referencing the client who made the payment
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)

    # Amount paid in the transaction
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    # Status of the payment (e.g., pending, completed, failed)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="pending")

    # Payment method used (e.g., credit card, PayPal)
    method: Mapped[str] = mapped_column(String(50), nullable=True)

    # Timestamp when the payment was created
    timestamp: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationship to the Client model
    client = relationship("Client", backref="payments")