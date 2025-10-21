from pydantic import BaseModel
from datetime import datetime


class StatisticWHBase(BaseModel):
    StatisticWHID: int


class StatisticWHResponse(StatisticWHBase):
    Date: datetime
    Height: int
    Weight: int

class StatisticWHRequest(StatisticWHBase):
    Date: datetime
    Height: int
    Weight: int