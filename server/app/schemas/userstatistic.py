from pydantic import BaseModel
from typing import Any
from datetime import datetime

class UserStatisticBase(BaseModel):
    UserID: int

class UserStatisticDTO(UserStatisticBase):
    Date: datetime 
    UserHeight: int 
    UserWeight: int 
    Calories: int 
    Protein: int 
    Fats: int 
    Carbonates: int 

    class Config:
        from_attributes = True