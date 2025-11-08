from sqlalchemy import or_
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

import hashlib
from typing import Union

from app.models.user import User
from app.schemas.user import UserDTO, UserDTOLogin, UserDTOAuth
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

    def edit_user(self, user_id: int, credentials: UserDTO):
        findedUser = self.db.query(User).filter(User.UserID == user_id).first()
        if not findedUser:
            raise ValueError
        
        findedUser.Email = credentials.Email
        findedUser.Phone = credentials.Phone

        self.db.commit()

        return findedUser

    def login(self, credentials: Union[UserDTOLogin, User]) -> Token:
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

    def refresh(self, access_token: str, refresh_token: str):
        security = Security(self.db)
        try:
            token = security.refresh_token(access_token, refresh_token)
        except:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token"
            )
        return token

    def auth(self, credentials: UserDTOAuth):

        tryFindUser = self.db.query(User).filter(or_(
            User.UserName == credentials.UserName,
            User.Email == credentials.Email
        )).first()

        if tryFindUser:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email or username already exist",
            )

        newUser = User(
            UserName=credentials.UserName,
            Salt=hashlib.sha256(b"change me pls").hexdigest(),
            Password=hashlib.sha256(credentials.Password.encode()).hexdigest(),
            Email=credentials.Email,
            Phone=credentials.Phone
        )

        self.db.add(newUser)
        self.db.commit()

        return newUser

    def logout(self, user: UserDTO):
        findedUser = self.db.query(User).filter(User.UserID == user.UserID).first()
        
        if not findedUser:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        
        findedUser.AccessToken = None
        findedUser.RefreshToken = None
        self.db.commit()

        return None