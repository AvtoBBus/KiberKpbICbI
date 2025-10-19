from pydantic import BaseModel
from datetime import datetime


class StatisticCPFCBase(BaseModel):
    StatisticCPFCID: int


class StatisticCPFCResponse(StatisticCPFCBase):
    Date: datetime
    Calories: int 
    Protein: int 
    Fat: int 
    Carbonates: int
