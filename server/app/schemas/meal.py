from pydantic import BaseModel, EmailStr
from typing import Any
from datetime import datetime


class MealBase(BaseModel):
    MealID: int

class MealResponse(MealBase):
    Date: datetime
    MealType: str

    class Config:
        from_attributes = True