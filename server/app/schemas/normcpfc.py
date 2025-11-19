from pydantic import BaseModel, EmailStr
from typing import Literal

class NormCPFCBase(BaseModel):
    NormID: int

class NormCPFCDTO(NormCPFCBase):
    Height: int
    Weight: int
    DesiredWeight: int
    Calories: int
    Protein: int
    Fats: int
    Carbonatest: int

    class Config:
        from_attributes = True


class NormCPFCDTOPost(NormCPFCBase):
    Height: int
    Weight: int
    DesiredWeight: int
    Activity: int
    Gender: Literal['м', 'ж']
    Age: int