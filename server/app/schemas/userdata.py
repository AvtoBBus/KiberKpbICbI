from pydantic import BaseModel
from typing import Any

class UserDataBase(BaseModel):
    UserDataID: int

class UserDataResponse(UserDataBase):
    Height: int
    Weight: int
    Age:int

class UserDataRequest(UserDataBase):
    Height: int
    Weight: int
    Age:int
