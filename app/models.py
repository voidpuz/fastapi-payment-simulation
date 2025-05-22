from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

import uuid
from datetime import datetime, timezone

from app.database import Base


class Merchant(Base):
    __tablename__ = "merchants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=True)
    api_key: Mapped[str] = mapped_column(String(50), nullable=False, default=uuid.uuid4().hex)
    callback_url: Mapped[str] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(String(50), nullable=False, default=datetime.now(timezone.utc))

    payments = relationship("Payment", back_populates="merchant")


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    merchant_id: Mapped[int] = mapped_column(Integer, ForeignKey("merchants.id"))
    merchant_order_id: Mapped[int] = mapped_column(nullable=False)
    amount: Mapped[int] = mapped_column(String(50), nullable=False)
    currency: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    callback_url: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(String(50), nullable=False, default=datetime.now(timezone.utc))

    merchant = relationship("Merchant", back_populates="payments")
    transactions = relationship("Transaction", back_populates="payment")


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    payment_id: Mapped[int] = mapped_column(Integer, ForeignKey("payments.id"))
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    auth_code: Mapped[str] = mapped_column(String(50), nullable=False)
    amount: Mapped[int] = mapped_column(String(50), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(String(50), nullable=False, default=datetime.now(timezone.utc))

    payment = relationship("Payment", back_populates="transactions")


class Card(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    merchant_id: Mapped[int] = mapped_column(Integer, ForeignKey("merchants.id"))
    masked_card_number: Mapped[str] = mapped_column(String(50), nullable=False)
    card_token: Mapped[str] = mapped_column(String(50), unique=True)
    created_at: Mapped[datetime] = mapped_column(String(50), nullable=False, default=datetime.now(timezone.utc))