from pydantic import BaseModel
from typing import Any
from datetime import datetime

class UserStatisticBase(BaseModel):
    UserID: int

class UserStatisticDTO(UserStatisticBase):
    Date: datetime 
    UserHeight: float 
    UserWeight: float 
    Calories: float 
    Protein: float 
    Fats: float 
    Carbonates: float 

    class Config:
        from_attributes = True