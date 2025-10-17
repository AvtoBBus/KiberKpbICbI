from pydantic import BaseModel, EmailStr
from typing import Any

class NormCPFCBase(BaseModel):
    NormID: int
    MinHeight: int
    MaxHeight: int
    MinWeight: int
    MaxWeight: int
    Calories: int
    Protein: int
    Fats: int
    Carbonatest: int

class NormCPFCResponse(NormCPFCBase):
    Goal: str

    class Config:
        from_attributes = True