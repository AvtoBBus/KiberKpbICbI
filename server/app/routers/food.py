from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.food import FoodResponse
from app.utils.db import get_db
from app.services.food import FoodService

router = APIRouter()

@router.get("/foods", response_model=List[FoodResponse])
def get_food(db: Session = Depends(get_db)):
    service = FoodService(db)
    foods = service.get_foods()
    return [
        FoodResponse(
            FoodID=food.FoodID,
            Name=food.Name,
            Category=food.Category.CategoryName
        ) for food in foods
    ]

@router.get("/foods/{food_id}", response_model=FoodResponse)
def get_food(food_id: int, db: Session = Depends(get_db)):
    service = FoodService(db)
    food = service.get_food(food_id)
    return FoodResponse(
        FoodID=food.FoodID,
        Name=food.Name,
        Category=food.Category.CategoryName
    )