from fastapi import APIRouter, Depends, HTTPException, status, Request, Response
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List, Annotated
from datetime import datetime

from app.schemas.meal import MealDTO, MealDTOPost, MealDTOPut
from app.utils.db import get_db
from app.utils.security import Security
from app.services.meal import MealService
from app.services.user import UserService


router = APIRouter()
oauth2_scheme = APIKeyHeader(name="token")

BASE_STR = "/meal"

@router.get(BASE_STR, response_model=List[MealDTO])
async def get_meal(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_db)
):
    
    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    service = MealService(db)
    meals = await service.get_meal(user.UserID)

    return [
        MealDTO(
            MealID = meal.MealID,
            Date = meal.Date,
            MealType = meal.MealType,
            Products=[
                {
                    'FoodID': fim.Food.FoodID,
                    'Name': fim.Food.Name,
                    'Weight': fim.Weight,
                    'Calories': fim.Food.Calories,
                    'Protein': fim.Food.Protein,
                    'Fats': fim.Food.Fats,
                    'Carbonates': fim.Food.Carbonates
                }
                for fim in meal.FoodInMeals
            ]
        ) for meal in meals
    ]

@router.get(BASE_STR + "/fromTo", response_model=List[MealDTO])
async def get_meal_by_date(
    token: Annotated[str, Depends(oauth2_scheme)],
    start_date: datetime,
    end_date: datetime,
    db: AsyncSession = Depends(get_db),
):
    
    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    if start_date > end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="StartDate must by below or equal EndDate"
        )

    service = MealService(db)
    meals = await service.get_meal_by_date(user.UserID, start_date, end_date)

    return [
        MealDTO(
            MealID = meal.MealID,
            Date = meal.Date,
            MealType = meal.MealType,
            Products=[
                {
                    'FoodID': fim.Food.FoodID,
                    'Name': fim.Food.Name,
                    'Weight': fim.Weight,
                    'Calories': fim.Food.Calories,
                    'Protein': fim.Food.Protein,
                    'Fats': fim.Food.Fats,
                    'Carbonates': fim.Food.Carbonates
                }
                for fim in meal.FoodInMeals
            ]
        ) for meal in meals
    ]

@router.get(BASE_STR + "/{meal_id}", response_model=MealDTO)
async def get_meal(
    meal_id: int,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_db)
):

    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    
    service = MealService(db)
    meal = await service.get_meal_id(user.UserID, meal_id)

    if not meal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Meal with id {meal_id} doesn't exist"
        )

    return MealDTO(
            MealID = meal.MealID,
            Date = meal.Date,
            MealType = meal.MealType,
            Products=[
                {
                    'FoodID': fim.Food.FoodID,
                    'Name': fim.Food.Name,
                    'Weight': fim.Weight,
                    'Calories': fim.Food.Calories,
                    'Protein': fim.Food.Protein,
                    'Fats': fim.Food.Fats,
                    'Carbonates': fim.Food.Carbonates
                }
                for fim in meal.FoodInMeals
            ]
        )

@router.post(BASE_STR, response_model=MealDTO)
async def add_meal(
    new_meal: MealDTOPost,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_db)
):
    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    service = MealService(db)
    try:
        inserted = await service.add_meal(user.UserID, new_meal)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Food with id {new_meal.FoodID} doesn`t exist"
        )

    return MealDTO(
            MealID = inserted.MealID,
            Date = inserted.Date,
            MealType = inserted.MealType,
            Products=[
                {
                    'FoodID': fim.Food.FoodID,
                    'Name': fim.Food.Name,
                    'Weight': fim.Weight,
                    'Calories': fim.Food.Calories,
                    'Protein': fim.Food.Protein,
                    'Fats': fim.Food.Fats,
                    'Carbonates': fim.Food.Carbonates
                }
                for fim in inserted.FoodInMeals
            ]
        )

@router.put(BASE_STR, response_model=MealDTO)
async def edit_meal(
    new_meal: MealDTOPut,
    token: Annotated[str, Depends(oauth2_scheme)], 
    db: AsyncSession = Depends(get_db)
):
    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    service = MealService(db)
    try:
        updated = await service.edit_meal(user.UserID, new_meal)
    except: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Meal with id {new_meal.MealID} doesn't exist"
        )

    return MealDTO(
            MealID = updated.MealID,
            Date = updated.Date,
            MealType = updated.MealType,
            Products=[
                {
                    'FoodID': fim.Food.FoodID,
                    'Name': fim.Food.Name,
                    'Weight': fim.Weight,
                    'Calories': fim.Food.Calories,
                    'Protein': fim.Food.Protein,
                    'Fats': fim.Food.Fats,
                    'Carbonates': fim.Food.Carbonates
                }
                for fim in updated.FoodInMeals
            ]
        )

@router.delete(BASE_STR + "/{meal_id}")
async def delete_meal(
    response: Response,
    meal_id: int,
    token: Annotated[str, Depends(oauth2_scheme)], 
    db: AsyncSession = Depends(get_db)
):
    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    service = MealService(db)
    try:
        await service.delete_meal(user.UserID, meal_id)
    except: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Meal with id {meal_id} doesn't exist"
        )

    response.status_code = status.HTTP_204_NO_CONTENT
    return None