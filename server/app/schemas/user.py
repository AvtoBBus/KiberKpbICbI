from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    UserID: int


class UserResponse(UserBase):
    UserName: str
    Email: str
    Phone: Optional[str]