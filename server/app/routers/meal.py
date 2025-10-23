from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List

from app.schemas.meal import MealDTO, MealDTOPost
from app.utils.db import get_db
from app.services.meal import MealService
from app.services.user import UserService

router = APIRouter()

BASE_STR = "/meal"

@router.get(BASE_STR + "/", response_model=List[MealDTO])
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
        MealDTO(
            MealID = meal.MealID,
            Date = meal.Date,
            MealType = meal.MealType
        ) for meal in meals
    ]

@router.get(BASE_STR + "/{meal_id}", response_model=MealDTO)
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

    return MealDTO(
        MealID = meal.MealID,
        Date = meal.Date,
        MealType = meal.MealType
    )

@router.post(BASE_STR + "/", response_model=MealDTO)
def add_meal(request: Request, new_meal: MealDTOPost, db: Session = Depends(get_db)):
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

@router.put(BASE_STR + "/", response_model=MealDTO)
def edit_meal(request: Request, new_meal: MealDTO, db: Session = Depends(get_db)):
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
    try:
        updated = service.edit_meal(user.UserID, new_meal)
    except: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Meal with id {new_meal.MealID} doesn't exist"
        )
    

    return updated