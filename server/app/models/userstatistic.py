from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum, Double
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from datetime import datetime
from typing import get_args

from .user import User

class UserStatistic(Base):
    __tablename__ = "userstatistic"
    
    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    UserID: Mapped[int] = mapped_column(Integer)
    Date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    UserHeight: Mapped[Double] = mapped_column(Double) 
    UserWeight: Mapped[Double] = mapped_column(Double) 
    Calories: Mapped[Double] = mapped_column(Double) 
    Protein: Mapped[Double] = mapped_column(Double) 
    Fats: Mapped[Double] = mapped_column(Double) 
    Carbonates: Mapped[Double] = mapped_column(Double) 
