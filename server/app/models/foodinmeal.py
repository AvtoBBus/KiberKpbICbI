from sqlalchemy import Column, ForeignKey, Integer, Enum, String
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped

from .food import Food
from .meal import Meal

class FoodInMeal(Base):
    __tablename__ = "foodinmeal"
    
    FoodInMealID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    ProductID: Mapped[int] = mapped_column(Integer)
    ProductName: Mapped[str] = mapped_column(String)
    Calories: Mapped[int] = mapped_column(Integer)
    Protein: Mapped[int] = mapped_column(Integer)
    Fats: Mapped[int] = mapped_column(Integer)
    Carbonates: Mapped[int] = mapped_column(Integer)
    
    MealID: Mapped[int] = mapped_column(ForeignKey("meal.MealID"))
    Meal: Mapped[list["Meal"]] = relationship(back_populates="FoodInMeals", lazy='joined')