from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    access_token_expires: str

class TokenDTO(BaseModel):
    token: str

class TokenRefreshDTO(BaseModel):
    refresh_token: str