from sqlalchemy import Column, ForeignKey, Integer, Enum, DateTime
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from datetime import datetime
from typing import Literal, get_args

from .user import User

MealTypeEnum = Literal["breakfast","lunch","dinner"]

class Meal(Base):
    __tablename__ = "meal"
    
    MealID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    MealType: Mapped[MealTypeEnum] = mapped_column(Enum(*get_args(MealTypeEnum)))

    UserID: Mapped[int] = mapped_column(ForeignKey("user.UserID"))