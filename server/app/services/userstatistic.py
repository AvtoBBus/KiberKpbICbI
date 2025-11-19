from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.userstatistic import UserStatistic

class UserStatisticService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_userstatistic(self, user_id: int):
        async with self.db as session:
            stmt = select(UserStatistic).where(UserStatistic.UserID == user_id)
            result = await session.execute(stmt)
            return result.scalars().all()