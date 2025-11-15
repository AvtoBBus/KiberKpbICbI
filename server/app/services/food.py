from sqlalchemy.ext.asyncio import AsyncSession
from app.models.food import Food
from app.schemas.food import FoodDTOPost
from sqlalchemy import Select
# from app.core.security import get_password_hash

class FoodService:
    def __init__(self, db: AsyncSession):
        self.db = db
       
    async def get_food_id(self, food_id: int):
        return self.db.query(Food).filter(Food.FoodID == food_id).first()
    
    async def get_food(self):
        async with self.db as session:
            return await session.execute(Select(Food))

    async def add_food(self, new_food: FoodDTOPost):

        inserted = Food(
            Name=new_food.Name,
            CategoryID=new_food.CategoryID,
            Calories=new_food.Calories,
            Protein=new_food.Protein,
            Fats=new_food.Fats,
            Carbonates=new_food.Carbonates
        )

        await self.db.add(inserted)
        await self.db.commit()

        return inserted