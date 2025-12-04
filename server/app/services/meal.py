from sqlalchemy.orm import Session
from app.models.meal import Meal
from app.models.foodinmeal import FoodInMeal
from app.models.food import Food
from app.schemas.meal import MealDTOPost

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
                selectinload(Meal.FoodInMeals)).where(Meal.MealID == meal_id)
            result = await session.execute(stmt)
            return result.scalars().first()

    async def get_meal(self, user_id: int) -> List[Meal]:
        async with self.db as session:
            stmt = select(Meal).where(Meal.UserID == user_id).options(
                selectinload(Meal.FoodInMeals))
            result = await session.execute(stmt)
            return result.scalars().all()

    async def get_meal_by_date(self, user_id: int, start_date: datetime, end_date: datetime) -> List[Meal]:
        async with self.db as session:
            stmt = select(Meal).where(and_(Meal.UserID == user_id, Meal.Date >= start_date, Meal.Date <= end_date)).options(
                selectinload(Meal.FoodInMeals).selectinload(FoodInMeal.Food))
            result = await session.execute(stmt)
            return result.scalars().all()

    async def get_meal_by_date_and_mealtype(self, user_id: int, start_date: datetime, end_date: datetime, meal_type: int) -> List[Meal]:
        async with self.db as session:
            stmt = select(Meal).where(and_(Meal.UserID == user_id,
                                            Meal.Date >= start_date,
                                            Meal.Date <= end_date,
                                            Meal.MealType == meal_type
                                        )).options(selectinload(Meal.FoodInMeals))
            result = await session.execute(stmt)
            return result.scalars().all()

    async def add_meal(self, user_id: int, new_meal: MealDTOPost):
        async with self.db as session:
            stmt = select(Meal).where(and_(Meal.UserID == user_id,
                                        Meal.Date == new_meal.Date,
                                        Meal.MealType == new_meal.MealType)).options(selectinload(Meal.FoodInMeals))
            result = await session.execute(stmt)
            findedMeal = result.scalars().first()

            if not findedMeal:
                findedMeal = Meal(
                    Date=new_meal.Date,
                    MealType=new_meal.MealType,
                    UserID=user_id
                )
                session.add(findedMeal)
                await session.flush()
                food_in_meals_count = 0
            else:
                food_in_meals_count = len(findedMeal.FoodInMeals)

            insertedFoodInMeal = FoodInMeal(
                MealID=findedMeal.MealID,
                ProductID=food_in_meals_count,
                ProductName=new_meal.Product.ProductName,
                Calories=new_meal.Product.Calories,
                Protein=new_meal.Product.Protein,
                Fats=new_meal.Product.Fats,
                Carbonates=new_meal.Product.Carbonates
            )
            session.add(insertedFoodInMeal)

            await session.commit()
            await session.refresh(findedMeal)

            return findedMeal

    async def delete_meal(self, user_id: int, meal_id: int):
        async with self.db as session:
            stmt = select(Meal).where(
                and_(Meal.UserID == user_id, Meal.MealID == meal_id))
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

    async def delete_product_in_meal(self, user_id: int, meal_id: int, product_id: int):
        async with self.db as session:
            stmt = select(Meal).where(and_(Meal.UserID == user_id, Meal.MealID == meal_id))
            result = await session.execute(stmt)
            findedMeal = result.scalars().first()

            if not findedMeal:
                raise ValueError
            
            stmt = select(FoodInMeal).where(and_(FoodInMeal.MealID == meal_id, FoodInMeal.ProductID == product_id))
            result = await session.execute(stmt)
            findedFoodInMeal = result.scalars().first()

            if not findedFoodInMeal:
                raise IndexError
            

            await session.delete(findedFoodInMeal)
            await session.commit()

            return None
        