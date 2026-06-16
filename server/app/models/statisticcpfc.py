from sqlalchemy import Column, ForeignKey, Double, String, DateTime
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from datetime import datetime

from .user import User


class StatisticCPFC(Base):
    __tablename__ = "statisticcpfc"

    StatisticCPFCID: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)

    Date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    Calories: Mapped[Double] = mapped_column(Double)
    Protein: Mapped[Double] = mapped_column(Double)
    Fats: Mapped[Double] = mapped_column(Double)
    Carbonates: Mapped[Double] = mapped_column(Double)

    UserID: Mapped[int] = mapped_column(ForeignKey("user.UserID"))
