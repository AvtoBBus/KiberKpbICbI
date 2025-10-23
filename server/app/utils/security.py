from datetime import datetime, timedelta, timezone
from typing import Union

from fastapi import status, HTTPException
from sqlalchemy.orm import Session

import jwt
import hashlib

from app.config import config
from app.schemas.user import UserDTO, UserDTOAuth
from app.schemas.token import Token
from app.utils.db import get_db
from app.models.user import User

class Security:

    def __init__(self, db: Session):
        self.db = db

    def create_access_token(self, data: dict, expires_delta: timedelta) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, config.settings.SECRET_KEY, algorithm=config.settings.ALGORITHM)
        return encoded_jwt

    def decode_token(self, token: str) -> UserDTO:
        return jwt.decode(token, config.settings.SECRET_KEY, algorithms=[config.settings.ALGORITHM])
        

    def login_for_access_token(self, email: str, password: str) -> Token:

        user: UserDTO = self.validate_user(email, password)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        access_token = self.create_access_token(
            data={
                "UserID": user.UserID,
                "Email": user.Email,
                "Phone": user.Phone
            },
            expires_delta=access_token_expires
        )

        return Token(
            access_token=access_token,
            token_type="Bearer",
            access_token_expires=str(access_token_expires)
        )

    def validate_user(self, email: str, password: str) -> Union[UserDTO, bool]:
        finded = self.db.query(User).filter(User.Email == email).first()

        user: UserDTO = UserDTO(
            UserID=finded.UserID,
            UserName=finded.UserName,
            Email=finded.Email,
            Phone=finded.Phone
        )

        if finded and finded.Password.__eq__(hashlib.sha256(password.encode()).hexdigest()):
            return user
        else:
            return False