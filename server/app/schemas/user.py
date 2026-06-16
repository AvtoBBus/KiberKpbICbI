from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    UserID: int

class UserDTO(UserBase):
    Email: EmailStr
    Phone: Optional[str]

class UserDTOLogin(BaseModel):
    Email: EmailStr
    Password: str

class UserDTOAuth(BaseModel):
    Email: EmailStr
    Password: str
