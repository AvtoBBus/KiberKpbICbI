from pydantic import BaseModel
from typing import Any, List
from datetime import datetime

class MealProduct(BaseModel):
    ProductID: int
    ProductName: str
    Calories: float
    Protein: float
    Fats: float
    Carbonates: float

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