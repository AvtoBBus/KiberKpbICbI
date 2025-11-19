from pydantic import BaseModel
from typing import Any

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

