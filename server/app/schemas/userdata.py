from pydantic import BaseModel
from typing import Any

class UserDataBase(BaseModel):
    UserDataID: int

class UserDataDTO(UserDataBase):
    Height: int
    Weight: int
    DesiredHeight: int
    DesiredWeight: int
    Activity: int
    Age:int
