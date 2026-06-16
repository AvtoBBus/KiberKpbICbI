from sqlalchemy import Column, ForeignKey, Integer, Enum, DateTime
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from datetime import datetime
from typing import get_args

from .user import User

class Meal(Base):
    __tablename__ = "meal"
    
    MealID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    MealType: Mapped[int] = mapped_column(Integer)

    UserID: Mapped[int] = mapped_column(ForeignKey("user.UserID"))
    FoodInMeals: Mapped[list["FoodInMeal"]] = relationship(back_populates="Meal", lazy='joined')