from pydantic import BaseModel, EmailStr
from typing import Any

class NormCPFCBase(BaseModel):
    NormID: int

class NormCPFCResponse(NormCPFCBase):
    MinHeight: int
    MaxHeight: int
    MinWeight: int
    MaxWeight: int
    Calories: int
    Protein: int
    Fats: int
    Carbonatest: int

    class Config:
        from_attributes = True

class NormCPFCRequest(NormCPFCBase):
    MinHeight: int
    MaxHeight: int
    MinWeight: int
    MaxWeight: int
    Calories: int
    Protein: int
    Fats: int
    Carbonatest: int

    class Config:
        from_attributes = True