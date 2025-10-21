from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.food import FoodResponse, FoodRequest
from app.utils.db import get_db
from app.services.food import FoodService

router = APIRouter()
BASE_STR = "/foods"

@router.get(f"{BASE_STR}", response_model=List[FoodResponse])
def get_food(db: Session = Depends(get_db)):
    service = FoodService(db)
    foods = service.get_food()
    return [
        FoodResponse(
            FoodID=food.FoodID,
            Name=food.Name,
            Category=food.Category.CategoryName,
            Calories=food.Calories,
            Protein=food.Protein,
            Fats=food.Fats,
            Carbonates=food.Carbonates
        ) for food in foods
    ]

@router.get(BASE_STR + "/{food_id}", response_model=FoodResponse)
def get_food(food_id: int, db: Session = Depends(get_db)):
    service = FoodService(db)
    food = service.get_food_id(food_id)
    return FoodResponse(
        FoodID=food.FoodID,
        Name=food.Name,
        Category=food.Category.CategoryName,
        Calories=food.Calories,
        Protein=food.Protein,
        Fats=food.Fats,
        Carbonates=food.Carbonates
    )

@router.post(f"{BASE_STR}", response_model=FoodResponse)
def add_food(new_food: FoodRequest, db: Session = Depends(get_db)):
    service = FoodService(db)
    inserted = service.add_food(new_food)
    return FoodResponse(
        FoodID=inserted.FoodID,
        Name=inserted.Name,
        Category=inserted.Category.CategoryName,
        Calories=inserted.Calories,
        Protein=inserted.Protein,
        Fats=inserted.Fats,
        Carbonates=inserted.Carbonates
    )