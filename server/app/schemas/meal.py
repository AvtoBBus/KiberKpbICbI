from pydantic import BaseModel
from typing import Any, List
from datetime import datetime

class MealProductBase(BaseModel):
    FoodID: int
    Weight: int

    class Config:
        from_attributes = True

class MealProduct(MealProductBase):
    Name: str
    Calories: int
    Protein: int
    Fats: int
    Carbonates: int

    class Config:
        from_attributes = True

class MealBase(BaseModel):
    MealID: int
    Date: datetime

class MealDTO(MealBase):
    MealType: int
    Products: List[MealProduct]

    class Config:
        from_attributes = True

class MealDTOPost(MealBase):
    MealType: int
    Products: List[MealProductBase]
    
    class Config:
        from_attributes = True

class MealDTOPut(MealBase):
    MealType: int
    Products: List[MealProductBase]


    class Config:
        from_attributes = True