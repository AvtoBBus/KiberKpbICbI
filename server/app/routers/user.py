from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from app.schemas.user import UserDTO, UserDTOLogin, UserDTOAuth
from app.schemas.token import Token, TokenRefreshDTO
from app.services.user import UserService
from app.utils.security import Security
from app.utils.db import get_db
from app.config import config

from typing import Annotated

router = APIRouter()

oauth2_scheme = APIKeyHeader(name="token")


@router.get("/user", response_model=UserDTO)
async def get_user(
    token: Annotated[str, Depends(oauth2_scheme)], 
    db: Session = Depends(get_db)
):
    service = UserService(db)
    security = Security(db)
    
    try:
        user = await service.get_user(token)
        checkToken = await security.check_user_token(token, user.UserID)
        if not checkToken:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    return UserDTO(
        UserID=user.UserID,
        Email=user.Email,
        Phone=user.Phone
    )


@router.post("/login", response_model=Token)
async def login(
    credentials: UserDTOLogin,
    db: Session = Depends(get_db)
):
    service = UserService(db)
    try:
        token = await service.login(credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return token

@router.put("/edit", response_model=UserDTO)
async def edit(
    credentials: UserDTO,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):
    
    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    if credentials.UserID != user.UserID:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect UserID"
        )

    service = UserService(db)
    try:
        newUser = await service.edit_user(user.UserID, credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad request",
        )
    
    return newUser


@router.post("/auth", response_model=Token)
async def auth(
    credentials: UserDTOAuth,
    db: Session = Depends(get_db)
):
    service = UserService(db)
    try:
        newUser = await service.auth(credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist",
        )

    token = await service.login(credentials)

    return token

@router.get("/logout")
async def logout(
    token: Annotated[str, Depends(oauth2_scheme)],
    response: Response,
    db: Session = Depends(get_db)
):
    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
        
        await auth.logout(user)
    except:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token"
        )


    response.status_code = status.HTTP_204_NO_CONTENT

    return None

@router.post("/refresh", response_model=Token)
async def refresh(
    refresh_token: TokenRefreshDTO,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):
    service = UserService(db)
    try:
        token = await service.refresh(token, refresh_token.refresh_token)
    except:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )

    return token

