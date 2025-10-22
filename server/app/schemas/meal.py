from pydantic import BaseModel, EmailStr
from typing import Any
from datetime import datetime


class MealBase(BaseModel):
    MealID: int
    Date: datetime

class MeaDTO(MealBase):
    MealType: str

    class Config:
        from_attributes = True

class MeaDTOPost(MealBase):
    MealType: str
    FoodID: int
    Weight: int

    class Config:
        from_attributes = True