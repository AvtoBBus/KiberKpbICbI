from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.userdata import UserDataResponse
from app.utils.db import get_db
from app.services.userdata import UserDataService

router = APIRouter()


@router.get("/userdata/{user_id}", response_model=List[UserDataResponse])
def get_userdata(user_id: int, db: Session = Depends(get_db)):
    service = UserDataService(db)
    data = service.get_userdata(user_id)
    return [
        UserDataResponse(
            UserDataID=userData.UserDataID,
            Height=userData.Height,
            Weight=userData.Weight,
            Age=userData.Age,
            Norm={
                "MinHeight": userData.Norm.MinHeight,
                "MaxHeight": userData.Norm.MaxHeight,
                "MinWeight": userData.Norm.MinWeight,
                "MaxWeight": userData.Norm.MaxWeight,
            }
        ) for userData in data
    ]


@router.get("/userdata/{user_id}/{user_data_id}", response_model=UserDataResponse)
def get_userdata_id(user_id: int, user_data_id: int, db: Session = Depends(get_db)):
    service = UserDataService(db)
    userData = service.get_userdata_id(user_id, user_data_id)
    return UserDataResponse(
        UserDataID=userData.UserDataID,
        Height=userData.Height,
        Weight=userData.Weight,
        Age=userData.Age,
        Norm={
            "MinHeight": userData.Norm.MinHeight,
            "MaxHeight": userData.Norm.MaxHeight,
            "MinWeight": userData.Norm.MinWeight,
            "MaxWeight": userData.Norm.MaxWeight,
        }
    )
