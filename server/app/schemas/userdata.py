from pydantic import BaseModel
from typing import Any

class UserDataBase(BaseModel):
    UserDataID: int
    Height: int
    Weight: int
    Age:int

class UserDataResponse(UserDataBase):
    Norm: Any

    class Config:
        from_attributes = True