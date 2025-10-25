from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.orm import Session

from app.schemas.user import UserDTO, UserDTOLogin, UserDTOAuth
from app.utils.db import get_db
from app.services.user import UserService
from app.config import config

router = APIRouter()


@router.get("/user", response_model=UserDTO)
def get_user(request: Request, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        token = request.cookies.get("token")
        user = service.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    return UserDTO(
        UserID=user.UserID,
        UserName=user.UserName,
        Email=user.Email,
        Phone=user.Phone
    )


@router.post("/login", response_model=UserDTO)
def login(
    credentials: UserDTOLogin,
    response: Response,
    db: Session = Depends(get_db)
):
    service = UserService(db)
    try:
        token = service.login(credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = service.get_user(token.access_token)

    response.set_cookie(
        key="token",
        value=token.access_token,
        max_age=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        domain="localhost",
        samesite="strict",
        httponly=True
    )

    return user

@router.put("/edit", response_model=UserDTO)
def edit(
    credentials: UserDTO,
    request: Request,
    db: Session = Depends(get_db)
):
    
    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
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
        newUser = service.edit_user(user.UserID, credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist",
        )
    
    return newUser


@router.post("/auth", response_model=UserDTO)
def auth(
    credentials: UserDTOAuth,
    response: Response,
    db: Session = Depends(get_db)
):
    service = UserService(db)
    try:
        newUser = service.auth(credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist",
        )

    token = service.login(credentials)

    response.set_cookie(
        key="token",
        value=token.access_token,
        max_age=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        domain="localhost",
        samesite="strict",
        httponly=True
    )

    return newUser


@router.get("/logout")
def logout(response: Response):
    response.delete_cookie(key="token")
    return None


