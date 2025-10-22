from pydantic import BaseModel
from datetime import datetime


class StatisticWHBase(BaseModel):
    StatisticWHID: int


class StatisticWHDTO(StatisticWHBase):
    Date: datetime
    Height: int
    Weight: int