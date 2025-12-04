from pydantic import BaseModel
from typing import Any, List
from datetime import datetime

class MealProduct(BaseModel):
    ProductID: int
    ProductName: str
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
    Date: datetime
    MealType: int
    Product: MealProduct
    
    class Config:
        from_attributes = True