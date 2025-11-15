from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.food import FoodDTO, FoodDTOPost
from app.utils.db import get_db
from app.services.food import FoodService

from typing import List
import asyncio

router = APIRouter()
BASE_STR = "/foods"

@router.get(f"{BASE_STR}", response_model=List[FoodDTO])
async def get_food(db: Session = Depends(get_db)):
    service = FoodService(db)
    foods = await service.get_food()
    print(foods)
    return [
        FoodDTO(
            FoodID=food.FoodID,
            Name=food.Name,
            Category=food.Category.CategoryName,
            Calories=food.Calories,
            Protein=food.Protein,
            Fats=food.Fats,
            Carbonates=food.Carbonates
        ) for food in foods
    ]

@router.get(BASE_STR + "/{food_id}", response_model=FoodDTO)
async def get_food(food_id: int, db: Session = Depends(get_db)):
    service = FoodService(db)
    food =  await service.get_food_id(food_id)
    return FoodDTO(
        FoodID=food.FoodID,
        Name=food.Name,
        Category=food.Category.CategoryName,
        Calories=food.Calories,
        Protein=food.Protein,
        Fats=food.Fats,
        Carbonates=food.Carbonates
    )

@router.post(f"{BASE_STR}", response_model=FoodDTO)
async def add_food(new_food: FoodDTOPost, db: Session = Depends(get_db)):
    service = FoodService(db)
    inserted =  await service.add_food(new_food)
    return FoodDTO(
        FoodID=inserted.FoodID,
        Name=inserted.Name,
        Category=inserted.Category.CategoryName,
        Calories=inserted.Calories,
        Protein=inserted.Protein,
        Fats=inserted.Fats,
        Carbonates=inserted.Carbonates
    )