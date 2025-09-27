from pydantic import BaseModel, EmailStr
from typing import Any

class FoodBase(BaseModel):
    FoodID: int
    Name: str

class FoodResponse(FoodBase):
    Category: str

    class Config:
        from_attributes = True