from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List
from app.schemas.userstatistic import UserStatisticDTO
from app.utils.db import get_db
from app.services.userstatistic import UserStatisticService
from app.services.user import UserService

router = APIRouter()

@router.get("/userstatistic", response_model=List[UserStatisticDTO])
def get_userstatistic(request: Request, db: Session = Depends(get_db)):

    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    service = UserStatisticService(db)
    stats = service.get_userstatistic(user.UserID)
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