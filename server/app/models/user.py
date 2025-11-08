from sqlalchemy import Column, ForeignKey, Integer, String
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from typing import Optional

class User(Base):
    __tablename__ = "user"
    
    UserID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    UserName: Mapped[str] = mapped_column(String)
    Salt: Mapped[str] = mapped_column(String)
    Password: Mapped[str] = mapped_column(String)
    Email: Mapped[str] = mapped_column(String)
    Phone: Mapped[Optional[str]] = mapped_column(default=None)
    AccessToken: Mapped[str] = mapped_column(String)
    RefreshToken: Mapped[str] = mapped_column(String)