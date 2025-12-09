from pydantic import BaseModel, EmailStr
from typing import Literal

class NormCPFCBase(BaseModel):
    NormID: int
    Height: float
    Weight: float
    DesiredWeight: float
    
class NormCPFCDTO(NormCPFCBase):
    Calories: float
    Protein: float
    Fats: float
    Carbonatest: float

    class Config:
        from_attributes = True


class NormCPFCDTOPost(NormCPFCBase):
    Activity: float
    Gender: Literal['м', 'ж']
    Age: float