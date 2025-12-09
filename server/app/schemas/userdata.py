from pydantic import BaseModel
from typing import Literal

class UserDataBase(BaseModel):
    UserDataID: int
    UserName: str
    Activity: int
    Age:int

class UserDataDTO(UserDataBase):
    Height: float
    Weight: float
    DesiredHeight: float
    DesiredWeight: float
    Gender: Literal['м', 'ж']

