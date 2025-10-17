from sqlalchemy import Column, ForeignKey, Integer, String
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped

class Food(Base):
    __tablename__ = "food"
    
    FoodID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Name: Mapped[str] = mapped_column(String)
    CategoryID: Mapped[int] = mapped_column(ForeignKey("foodcategories.CategoryID"))
    Category: Mapped["FoodCategory"] = relationship(back_populates="Food")
    Calories: Mapped[int] = mapped_column(Integer)
    Protein: Mapped[int] = mapped_column(Integer)
    Fats: Mapped[int] = mapped_column(Integer)
    Carbonatest: Mapped[int] = mapped_column(Integer)


class FoodCategory(Base):
    __tablename__ = "foodcategories"
    
    CategoryID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    CategoryName: Mapped[str] = mapped_column(String)
    Food: Mapped[list["Food"]] = relationship(back_populates="Category")    