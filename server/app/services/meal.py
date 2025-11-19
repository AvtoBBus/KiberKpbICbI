from sqlalchemy.orm import Session
from app.models.meal import Meal
from app.models.foodinmeal import FoodInMeal
from app.models.food import Food
from app.schemas.meal import MealDTOPut, MealDTOPost

from datetime import datetime
from typing import List, Any

from sqlalchemy.orm import selectinload
from sqlalchemy import select, and_, delete
from sqlalchemy.ext.asyncio import AsyncSession

class MealService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_meal_id(self, user_id: int, meal_id: int):
        async with self.db as session:
            stmt = select(Meal).where(Meal.UserID == user_id).options(
                selectinload(Meal.FoodInMeals).selectinload(FoodInMeal.Food)).where(Meal.MealID == meal_id)
            result = await session.execute(stmt)
            return result.scalars().first()

    async def get_meal(self, user_id: int) -> List[Any]:
        async with self.db as session:
            stmt = select(Meal).where(Meal.UserID == user_id).options(
                selectinload(Meal.FoodInMeals).selectinload(FoodInMeal.Food))
            print(stmt)
            result = await session.execute(stmt)
            return result.scalars().all()
        
    async def get_meal_by_date(self, user_id: int, start_date: datetime, end_date: datetime) -> List[Any]:
        async with self.db as session:
            stmt = select(Meal).where(and_(Meal.UserID == user_id, Meal.Date >= start_date, Meal.Date <= end_date)).options(
                selectinload(Meal.FoodInMeals).selectinload(FoodInMeal.Food))
            print(stmt)
            result = await session.execute(stmt)
            return result.scalars().all()

    async def add_meal(self, user_id: int, new_meal: MealDTOPost):
        async with self.db as session:

            insertedMeal = Meal(
                Date=new_meal.Date,
                MealType=new_meal.MealType,
                UserID=user_id
            )

            session.add(insertedMeal)
            await session.flush()

            for i in range(len(new_meal.Products)):
                insertedFoodInMeal = FoodInMeal(
                    MealID=insertedMeal.MealID,
                    FoodID=new_meal.Products[i].FoodID,
                    Weight=new_meal.Products[i].Weight
                )

                session.add(insertedFoodInMeal)
            
            await session.commit()
            await session.refresh(insertedMeal)

            return insertedMeal

    async def edit_meal(self, user_id: int, new_meal: MealDTOPut):
        async with self.db as session:
            stmt = select(Meal).where(and_(Meal.UserID == user_id, Meal.MealID == new_meal.MealID))
            result = await session.execute(stmt)
            findedMeal = result.scalars().first()

            if not findedMeal:
                raise ValueError

            findedMeal.MealType = new_meal.MealType
            findedMeal.Date = new_meal.Date

            stmt = delete(FoodInMeal).where(FoodInMeal.MealID == new_meal.MealID)
            await session.execute(stmt)

            for product in new_meal.Products:
                stmt = select(Food).where(Food.FoodID == product.FoodID)
                result = await session.execute(stmt)
                findedFood = result.scalars().first()

                if not findedFood:
                    raise ValueError

                insertedFoodInMeal = FoodInMeal(
                    MealID=new_meal.MealID,
                    FoodID=product.FoodID,
                    Weight=product.Weight
                )
                session.add(insertedFoodInMeal)

            await session.commit()
            await session.refresh(findedMeal)

            return findedMeal

    async def delete_meal(self, user_id: int, meal_id: int):
        async with self.db as session:
            stmt = select(Meal).where(and_(Meal.UserID == user_id, Meal.MealID == meal_id))
            result = await session.execute(stmt)
            findedMeal = result.scalars().first()

            stmt = select(FoodInMeal).where(FoodInMeal.MealID == meal_id)
            result = await session.execute(stmt)
            findedFoodInMeal = result.scalars().unique().all()

            if (not findedMeal) or (len(findedFoodInMeal) == 0):
                raise ValueError

            await session.delete(findedMeal)
            for fim in findedFoodInMeal:
                await self.db.delete(fim)

            await session.commit()

            return None
