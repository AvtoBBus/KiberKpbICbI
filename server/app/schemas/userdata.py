from pydantic import BaseModel
from typing import Literal

class UserDataBase(BaseModel):
    UserDataID: int

class UserDataDTO(UserDataBase):
    UserName: str
    Activity: int
    Age:int
    Height: int
    Weight: int
    DesiredHeight: int
    DesiredWeight: int
    Gender: Literal['м', 'ж']

