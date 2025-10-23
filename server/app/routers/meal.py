from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List

from app.schemas.meal import MeaDTO, MeaDTOPost
from app.utils.db import get_db
from app.services.meal import MealService
from app.services.user import UserService

router = APIRouter()

BASE_STR = "/meal"

@router.get(BASE_STR + "/", response_model=List[MeaDTO])
def get_meal(request: Request, db: Session = Depends(get_db)):
    
    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    service = MealService(db)
    meals = service.get_meal(user.UserID)
    return [
        MeaDTO(
            MealID = meal.MealID,
            Date = meal.Date,
            MealType = meal.MealType
        ) for meal in meals
    ]

@router.get(BASE_STR + "/{meal_id}", response_model=MeaDTO)
def get_meal(request: Request, meal_id: int, db: Session = Depends(get_db)):

    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    
    service = MealService(db)
    meal = service.get_meal_id(user.UserID, meal_id)

    if not meal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Meal with id {meal_id} doesn't exist"
        )

    return MeaDTO(
        MealID = meal.MealID,
        Date = meal.Date,
        MealType = meal.MealType
    )

@router.post(BASE_STR + "/", response_model=MeaDTO)
def add_meal(request: Request, new_meal: MeaDTOPost, db: Session = Depends(get_db)):

    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    service = MealService(db)
    inserted = service.add_meal(user.UserID, new_meal)

    return inserted