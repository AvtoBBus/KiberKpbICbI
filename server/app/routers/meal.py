from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.meal import MealResponse, MealRequest
from app.utils.db import get_db
from app.services.meal import MealService

router = APIRouter()

BASE_STR = "/meal"

@router.get(BASE_STR + "/{user_id}", response_model=List[MealResponse])
def get_meal(user_id: int, db: Session = Depends(get_db)):
    service = MealService(db)
    meals = service.get_meal(user_id)
    return [
        MealResponse(
            MealID = meal.MealID,
            Date = meal.Date,
            MealType = meal.MealType
        ) for meal in meals
    ]

@router.get(BASE_STR + "/{user_id}/{meal_id}", response_model=MealResponse)
def get_meal(user_id: int, meal_id: int, db: Session = Depends(get_db)):
    service = MealService(db)
    meal = service.get_meal_id(user_id, meal_id)
    return MealResponse(
        MealID = meal.MealID,
        Date = meal.Date,
        MealType = meal.MealType
    )

@router.post(BASE_STR + "/{user_id}", response_model=MealResponse)
def add_meal(user_id: int, new_meal: MealRequest, db: Session = Depends(get_db)):
    service = MealService(db)
    inserted = service.add_meal(user_id, new_meal)

    return inserted