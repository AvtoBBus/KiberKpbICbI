from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import UserResponse
from app.utils.db import get_db
from app.services.user import UserService

router = APIRouter()


@router.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user(user_id)
    return UserResponse(
        UserID=user.UserID,
        UserName=user.UserName,
        Email=user.Email,
        Phone=user.Phone
    )
