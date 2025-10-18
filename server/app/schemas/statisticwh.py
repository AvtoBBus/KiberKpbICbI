from pydantic import BaseModel
from datetime import datetime


class StatisticWhBase(BaseModel):
    StatisticWHID: int


class StatisticWhResponse(StatisticWhBase):
    Date: datetime
    Height: int
    Weight: int
