from sqlalchemy import Column, ForeignKey, Integer, Enum, DateTime
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped

from .food import Food
from .meal import Meal

class FoodInMeal(Base):
    __tablename__ = "foodinmeal"
    
    FoodInMealID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Weight: Mapped[int] = mapped_column(Integer)

    FoodID: Mapped[int] = mapped_column(ForeignKey("food.FoodID"))
    Food: Mapped[list["Food"]] = relationship(back_populates="FoodInMeals")

    MealID: Mapped[int] = mapped_column(ForeignKey("meal.MealID"))
    Meal: Mapped[list["Meal"]] = relationship(back_populates="FoodInMeals")