from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from typing import Union, Any, Annotated

from app.schemas.user import UserDTO, UserDTOLogin
from app.utils.db import get_db
from app.services.user import UserService
from app.config import config

router = APIRouter()

auth = HTTPBasic()

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
        response.delete_cookie(
            key="token",
            domain="localhost",
            samesite="strict",
            httponly=True
        )
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    user = service.get_user(token.access_token)

    response.set_cookie(
        key="token",
        value=token.access_token,
        domain="localhost",
        samesite="strict",
        httponly=True
    )
    
    return user

