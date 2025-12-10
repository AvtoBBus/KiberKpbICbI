from fastapi import APIRouter, Depends, HTTPException, status, Request, Response
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List, Annotated
from datetime import datetime

from app.schemas.meal import MealDTO, MealDTOPost
from app.utils.db import get_db
from app.utils.security import Security
from app.services.meal import MealService
from app.services.user import UserService

from app.services.statisticcpfc import StatisticCPFCService
from app.schemas.statisticcpfc import StatisticCPFCDTO

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
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
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
                    'ProductID': fim.ProductID,
                    'ProductName': fim.ProductName,
                    'Calories': fim.Calories,
                    'Protein': fim.Protein,
                    'Fats': fim.Fats,
                    'Carbonates': fim.Carbonates
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
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )
    
    if start_date > end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={ "message": "Дата начала должна быть раньше или равна дате конца" }
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
                    'ProductID': fim.ProductID,
                    'ProductName': fim.ProductName,
                    'Calories': fim.Calories,
                    'Protein': fim.Protein,
                    'Fats': fim.Fats,
                    'Carbonates': fim.Carbonates
                }
                for fim in meal.FoodInMeals
            ]
        ) for meal in meals
    ]

@router.get(BASE_STR + "/fromTo/{meal_type}", response_model=List[MealDTO])
async def get_meal_by_date_and_mealtype(
    token: Annotated[str, Depends(oauth2_scheme)],
    start_date: datetime,
    end_date: datetime,
    meal_type: int,
    db: AsyncSession = Depends(get_db),
):
        
    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )
    
    if start_date > end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={ "message": "Дата начала должна быть раньше или равна дате конца" }
        )

    service = MealService(db)
    meals = await service.get_meal_by_date_and_mealtype(user.UserID, start_date, end_date, meal_type)

    return [
        MealDTO(
            MealID = meal.MealID,
            Date = meal.Date,
            MealType = meal.MealType,
            Products=[
                {
                    'ProductID': fim.ProductID,
                    'ProductName': fim.ProductName,
                    'Calories': fim.Calories,
                    'Protein': fim.Protein,
                    'Fats': fim.Fats,
                    'Carbonates': fim.Carbonates
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
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )

    
    service = MealService(db)
    meal = await service.get_meal_id(user.UserID, meal_id)

    if not meal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={ "message": f"Не удалось найти прием пищи с id {meal_id}" }
        )

    return MealDTO(
            MealID = meal.MealID,
            Date = meal.Date,
            MealType = meal.MealType,
            Products=[
                {
                    'ProductID': fim.ProductID,
                    'ProductName': fim.ProductName,
                    'Calories': fim.Calories,
                    'Protein': fim.Protein,
                    'Fats': fim.Fats,
                    'Carbonates': fim.Carbonates
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
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )

    service = MealService(db)
    inserted = await service.add_meal(user.UserID, new_meal)

    statCPFC = StatisticCPFCService(db)
    prevStat = await statCPFC.get_statisticcpfc_by_date(user.UserID, new_meal.Date, new_meal.Date)

    if prevStat[0].StatisticCPFCID == -1:
        newStatCPFC = StatisticCPFCDTO(
            StatisticCPFCID=0,
            Date=new_meal.Date,
            Calories=new_meal.Product.Calories,
            Protein=new_meal.Product.Protein,
            Fats=new_meal.Product.Fats,
            Carbonates=new_meal.Product.Carbonates
        )
        await statCPFC.add_statisticcpfc(user.UserID, newStatCPFC)
    else:
        prevStat[0].Calories += new_meal.Product.Calories
        prevStat[0].Protein += new_meal.Product.Protein
        prevStat[0].Fats += new_meal.Product.Fats
        prevStat[0].Carbonates += new_meal.Product.Carbonates
        await statCPFC.edit_statisticcpfc(user.UserID, prevStat[0])

    return MealDTO(
            MealID = inserted.MealID,
            Date = inserted.Date,
            MealType = inserted.MealType,
            Products=[
                {
                    'ProductID': fim.ProductID,
                    'ProductName': fim.ProductName,
                    'Calories': fim.Calories,
                    'Protein': fim.Protein,
                    'Fats': fim.Fats,
                    'Carbonates': fim.Carbonates
                }
                for fim in inserted.FoodInMeals
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
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )
    
    service = MealService(db)
    try:
        findedMeal = await service.get_meal_id(user.UserID, meal_id)

        if findedMeal:
            statCPFC = StatisticCPFCService(db)
            prevStat = await statCPFC.get_statisticcpfc_by_date(user.UserID, findedMeal.Date, findedMeal.Date)

            SumCalories = 0
            SumProtein = 0
            SumFats = 0
            SumCarbonates = 0

            for fim in findedMeal.FoodInMeals:
                SumCalories += fim.Calories
                SumProtein += fim.Protein
                SumFats += fim.Fats
                SumCarbonates += fim.Carbonates


            prevStat[0].Calories -= SumCalories
            prevStat[0].Protein -= SumProtein
            prevStat[0].Fats -= SumFats
            prevStat[0].Carbonates -= SumCarbonates

            await service.delete_meal(user.UserID, meal_id)
            await statCPFC.edit_statisticcpfc(user.UserID, prevStat[0])

        else:
            raise ValueError

    except: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={ "message": f"Не удалось найти прием пищи с id {meal_id}" }
        )

    response.status_code = status.HTTP_204_NO_CONTENT
    return None

@router.delete(BASE_STR + "/{meal_id}/{product_id}")
async def delete_product_in_meal(
    response: Response,
    meal_id: int,
    product_id: int,
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
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )
    
    service = MealService(db)
    try:

        findedMeal = await service.get_meal_id(user.UserID, meal_id)

        if findedMeal:
            statCPFC = StatisticCPFCService(db)
            prevStat = await statCPFC.get_statisticcpfc_by_date(user.UserID, findedMeal.Date, findedMeal.Date)

            findedFim = None

            for fim in findedMeal.FoodInMeals:
                if fim.ProductID == product_id:
                    findedFim = fim
                    break

            if not findedFim:
                raise IndexError
            

            prevStat[0].Calories -= findedFim.Calories
            prevStat[0].Protein -= findedFim.Protein
            prevStat[0].Fats -= findedFim.Fats
            prevStat[0].Carbonates -= findedFim.Carbonates

            await service.delete_product_in_meal(user.UserID, meal_id, product_id)
            await statCPFC.edit_statisticcpfc(user.UserID, prevStat[0])

        else:
            raise ValueError

    except ValueError: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={ "message": f"Не удалось найти прием пищи с id {meal_id}" }
        )
    except IndexError: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={ "message": f"Не удалось найти продукт с id {product_id} в приеме пищи с id {meal_id}" }
        )

    response.status_code = status.HTTP_204_NO_CONTENT
    return None