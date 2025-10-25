from fastapi import APIRouter, Depends, HTTPException, status, Request,Response
from sqlalchemy.orm import Session
from typing import List

from app.schemas.meal import MealDTO, MealDTOPost, MealDTOPut
from app.utils.db import get_db
from app.services.meal import MealService
from app.services.user import UserService

from app.utils.mealtype import MealTypeEnum

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
    
    if not new_meal.MealType in MealTypeEnum.__args__:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Bad meal type"
        )

    service = MealService(db)
    try:
        inserted = service.add_meal(user.UserID, new_meal)
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

@router.put(BASE_STR + "/", response_model=MealDTO)
def edit_meal(request: Request, new_meal: MealDTOPut, db: Session = Depends(get_db)):
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
def delete_meal(request: Request, response: Response, meal_id: int, db: Session = Depends(get_db)):
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
        service.delete_meal(user.UserID, meal_id)
    except: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Meal with id {meal_id} doesn't exist"
        )

    response.status_code = status.HTTP_204_NO_CONTENT
    return None