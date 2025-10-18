from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from datetime import datetime

from .user import User


class StatisticWh(Base):
    __tablename__ = "statisticwh"

    StatisticWHID: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)

    Date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    Height: Mapped[int] = mapped_column(Integer)
    Weight: Mapped[int] = mapped_column(Integer)

    UserID: Mapped[int] = mapped_column(ForeignKey("user.UserID"))
