from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from datetime import datetime

from .user import User


class StatisticCPFC(Base):
    __tablename__ = "statisticcpfc"

    StatisticCPFCID: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)

    Date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    Calories: Mapped[int] = mapped_column(Integer)
    Protein: Mapped[int] = mapped_column(Integer)
    Fats: Mapped[int] = mapped_column(Integer)
    Carbonates: Mapped[int] = mapped_column(Integer)

    UserID: Mapped[int] = mapped_column(ForeignKey("user.UserID"))
