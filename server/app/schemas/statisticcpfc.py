from pydantic import BaseModel
from datetime import datetime


class StatisticCPFCBase(BaseModel):
    StatisticCPFCID: int


class StatisticCPFCDTO(StatisticCPFCBase):
    Date: datetime
    Calories: int 
    Protein: int 
    Fats: int 
    Carbonates: int