from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.food import FoodDTO, FoodDTOPost
from app.utils.db import get_db
from app.services.food import FoodService

from typing import List

router = APIRouter()
BASE_STR = "/foods"

@router.get(f"{BASE_STR}", response_model=List[FoodDTO])
async def get_food(db: AsyncSession = Depends(get_db)):
    service = FoodService(db)
    foods = await service.get_food()
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
async def get_food(food_id: int, db: AsyncSession = Depends(get_db)):
    service = FoodService(db)
    food =  await service.get_food_id(food_id)
    if not food:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Food with id {food_id} not found"
        )
    
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
async def add_food(new_food: FoodDTOPost, db: AsyncSession = Depends(get_db)):
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