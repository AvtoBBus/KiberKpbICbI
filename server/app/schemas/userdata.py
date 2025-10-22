from pydantic import BaseModel
from typing import Any

class UserDataBase(BaseModel):
    UserDataID: int

class UserDataDTO(UserDataBase):
    Height: int
    Weight: int
    Age:int
