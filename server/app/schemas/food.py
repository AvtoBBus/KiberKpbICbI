from pydantic import BaseModel, EmailStr
from typing import Any

class FoodBase(BaseModel):
    FoodID: int
    Name: str
    Calories: int
    Protein: int
    Fats: int
    Carbonates: int 

class FoodResponse(FoodBase):
    Category: str

    class Config:
        from_attributes = True

class FoodRequest(FoodBase):
    CategoryID: int
    
    class Config:
        from_attributes = True