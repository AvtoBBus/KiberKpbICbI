from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.security import HTTPBasicCredentials

from app.models.user import User
from app.schemas.user import UserDTO, UserDTOLogin
from app.schemas.token import Token

from app.utils.security import Security


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, token: str) -> UserDTO:
        security = Security(self.db)
        try:
            finded = security.decode_token(token)
        except:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
        
        return self.db.query(User).filter(User.UserID == finded.get("UserID")).first()

    def login(self, credentials: UserDTOLogin) -> Token:
        security = Security(self.db)
        try:
            token = security.login_for_access_token(
                email=credentials.Email, password=credentials.Password)
        except:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return token
