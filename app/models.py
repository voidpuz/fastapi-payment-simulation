from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.database import Base


# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(50))
#     email: Mapped[str] = mapped_column(String(50))