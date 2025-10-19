from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.meal import MealResponse
from app.utils.db import get_db
from app.services.meal import MealService

router = APIRouter()

@router.get("/meal/{user_id}", response_model=List[MealResponse])
def get_food(user_id: int, db: Session = Depends(get_db)):
    service = MealService(db)
    meals = service.get_meal(user_id)
    return [
        MealResponse(
            MealID = meal.MealID,
            Date = meal.Date,
            MealType = meal.MealType
        ) for meal in meals
    ]

@router.get("/meal/{user_id}/{meal_id}", response_model=MealResponse)
def get_food(user_id: int, meal_id: int, db: Session = Depends(get_db)):
    service = MealService(db)
    meal = service.get_meal_id(user_id, meal_id)
    return MealResponse(
        MealID = meal.MealID,
        Date = meal.Date,
        MealType = meal.MealType
    )