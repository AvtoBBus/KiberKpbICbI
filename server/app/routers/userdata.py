from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List

from app.schemas.userdata import UserDataDTO, UserDataDTO
from app.utils.db import get_db
from app.services.userdata import UserDataService
from app.services.user import UserService

router = APIRouter()


@router.get("/userdata", response_model=List[UserDataDTO])
def get_userdata(request: Request, db: Session = Depends(get_db)):

    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    service = UserDataService(db)
    data = service.get_userdata(user.UserID)

    return [
        UserDataDTO(
            UserDataID=userData.UserDataID,
            Height=userData.Height,
            Weight=userData.Weight,
            Age=userData.Age,
        ) for userData in data
    ]


@router.get("/userdata/{user_data_id}", response_model=UserDataDTO)
def get_userdata_id(request: Request, user_data_id: int, db: Session = Depends(get_db)):
    
    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    service = UserDataService(db)
    userData = service.get_userdata_id(user.UserID, user_data_id)
    return UserDataDTO(
        UserDataID=userData.UserDataID,
        Height=userData.Height,
        Weight=userData.Weight,
        Age=userData.Age,
    )


@router.post("/userdata", response_model=UserDataDTO)
def add_userdata(request: Request, new_user_data: UserDataDTO, db: Session = Depends(get_db)):
        
    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    service = UserDataService(db)
    inserted = service.add_userdata(user.UserID, new_user_data)
    return UserDataDTO(
        UserDataID=inserted.UserDataID,
        Height=inserted.Height,
        Weight=inserted.Weight,
        Age=inserted.Age,
    )

