from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.userdata import UserDataDTO, UserDataDTO
from app.utils.db import get_db
from app.services.userdata import UserDataService

router = APIRouter()


@router.get("/userdata/{user_id}", response_model=List[UserDataDTO])
def get_userdata(user_id: int, db: Session = Depends(get_db)):
    service = UserDataService(db)
    data = service.get_userdata(user_id)
    return [
        UserDataDTO(
            UserDataID=userData.UserDataID,
            Height=userData.Height,
            Weight=userData.Weight,
            Age=userData.Age,
        ) for userData in data
    ]


@router.get("/userdata/{user_id}/{user_data_id}", response_model=UserDataDTO)
def get_userdata_id(user_id: int, user_data_id: int, db: Session = Depends(get_db)):
    service = UserDataService(db)
    userData = service.get_userdata_id(user_id, user_data_id)
    return UserDataDTO(
        UserDataID=userData.UserDataID,
        Height=userData.Height,
        Weight=userData.Weight,
        Age=userData.Age,
    )


@router.post("/userdata/{user_id}", response_model=UserDataDTO)
def get_userdata_id(user_id: int, new_user_data: UserDataDTO, db: Session = Depends(get_db)):
    service = UserDataService(db)
    inserted = service.add_userdata(user_id, new_user_data)
    return UserDataDTO(
        UserDataID=inserted.UserDataID,
        Height=inserted.Height,
        Weight=inserted.Weight,
        Age=inserted.Age,
    )

