from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from datetime import datetime
from typing import get_args

from app.utils.mealtype import MealTypeEnum

from .user import User

class UserStatistic(Base):
    __tablename__ = "userstatistic"
    
    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    UserID: Mapped[int] = mapped_column(Integer)
    Date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    UserHeight: Mapped[int] = mapped_column(Integer) 
    UserWeight: Mapped[int] = mapped_column(Integer) 
    Calories: Mapped[int] = mapped_column(Integer) 
    Protein: Mapped[int] = mapped_column(Integer) 
    Fat: Mapped[int] = mapped_column(Integer) 
    Carbonates: Mapped[int] = mapped_column(Integer) 
    MealType: Mapped[MealTypeEnum] = mapped_column(Enum(*get_args(MealTypeEnum)))
    FoodWeight: Mapped[int] = mapped_column(Integer) 
