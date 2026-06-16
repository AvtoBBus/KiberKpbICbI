from app.models.food import Food
from app.schemas.food import FoodDTOPost

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

class FoodService:
    def __init__(self, db: AsyncSession):
        self.db = db
       
    async def get_food_id(self, food_id: int):
        async with self.db as session:
            stmt = select(Food).where(Food.FoodID == food_id).options(selectinload(Food.Category))
            result = await session.execute(stmt)
            data = result.scalars().first()
            return data

    
    async def get_food(self):
        async with self.db as session:
            stmt = select(Food).options(selectinload(Food.Category))
            result = await session.execute(stmt)
            data = result.scalars().all()
            return data

    async def add_food(self, new_food: FoodDTOPost):

        async with self.db as session:
            inserted = Food(
                Name=new_food.Name,
                CategoryID=new_food.CategoryID,
                Calories=new_food.Calories,
                Protein=new_food.Protein,
                Fats=new_food.Fats,
                Carbonates=new_food.Carbonates
            )

            session.add(inserted)
            await session.commit()
            await session.refresh(inserted, ['Category'])

            return inserted