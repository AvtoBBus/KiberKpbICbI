from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

import hashlib
from typing import Union

from app.models.user import User
from app.schemas.user import UserDTO, UserDTOLogin, UserDTOAuth
from app.schemas.token import Token
from app.utils.security import Security


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user(self, token: str) -> UserDTO:
        async with self.db as session:
            security = Security(session)
            try:
                finded = security.decode_token(token)
            except:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect token",
            )

            stmt = select(User).where(User.UserID == finded.get("UserID"))
            result = await session.execute(stmt)
            data = result.scalars().first()

            if data.AccessToken is None or not data.AccessToken.__eq__(token):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Unauthorized"
                )

            return data

    async def edit_user(self, user_id: int, credentials: UserDTO):
        async with self.db as session:

            stmt = select(User).where(User.UserID == user_id)
            result = await session.execute(stmt)
            findedUser = result.scalars().first()

            if not findedUser:
                raise ValueError
            
            findedUser.Email = credentials.Email
            findedUser.Phone = credentials.Phone

            await session.commit()
            await session.refresh(findedUser)

            return findedUser

    async def login(self, credentials: Union[UserDTOLogin, User]) -> Token:
        async with self.db as session:
            security = Security(session)
            try:
                token = await security.login_for_access_token(
                    email=credentials.Email, password=credentials.Password)
            except:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect email or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return token

    async def refresh(self, access_token: str, refresh_token: str):
        async with self.db as session:
            security = Security(session)
            try:
                token = await security.refresh_token(access_token, refresh_token)
            except:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token"
                )
            return token

    async def auth(self, credentials: UserDTOAuth):
        async with self.db as session:
            stmt = select(User).where(User.Email == credentials.Email)
            result = await session.execute(stmt)

            tryFindUser = result.scalars().first()

            if tryFindUser is not None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email already exist",
                )
            
            newUser = User(
                Salt=hashlib.sha256(b"change me pls").hexdigest(),
                Password=hashlib.sha256(credentials.Password.encode()).hexdigest(),
                Email=credentials.Email,
                Phone=None
            )

            session.add(newUser)
            await session.commit()
            await session.refresh(newUser)

            return newUser

    async def logout(self, user: UserDTO):
        async with self.db as session:
            stmt = select(User).where(User.UserID == user.UserID)
            result = await session.execute(stmt)

            findedUser = result.scalars().first()
            
            if not findedUser:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN
                )
            
            findedUser.AccessToken = None
            findedUser.RefreshToken = None
            await session.commit()
            await session.refresh(findedUser)

            return None