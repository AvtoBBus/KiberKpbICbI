from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.userstatistic import UserStatisticDTO
from app.utils.db import get_db
from app.services.userstatistic import UserStatisticService

router = APIRouter()

@router.get("/userstatistic/{user_id}", response_model=List[UserStatisticDTO])
def get_userdata(user_id: int, db: Session = Depends(get_db)):
    service = UserStatisticService(db)
    stats = service.get_userstatistic(user_id)
    return [
        UserStatisticDTO(
            UserID=userstatistic.UserID,
            Date= userstatistic.Date,
            UserHeight= userstatistic.UserHeight,
            UserWeight=userstatistic.UserWeight,
            Calories=userstatistic.Calories,
            Protein=userstatistic.Protein,
            Fat=userstatistic.Fat,
            Carbonates=userstatistic.Carbonates,
            MealType=userstatistic.MealType,
            FoodWeight=userstatistic.FoodWeight
        ) for userstatistic in stats
    ]