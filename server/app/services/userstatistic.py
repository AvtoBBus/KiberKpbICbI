from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.userstatistic import UserStatistic

from datetime import datetime


class UserStatisticService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_userstatistic(self, user_id: int):
        async with self.db as session:
            stmt = select(UserStatistic).where(UserStatistic.UserID == user_id)
            result = await session.execute(stmt)
            return result.scalars().all()

    async def get_userstatistic_by_date(self, user_id: int, start_date: datetime, end_date: datetime):
        async with self.db as session:
            stmt = select(UserStatistic).where(and_(UserStatistic.UserID == user_id,
                                                    UserStatistic.Date >= start_date, UserStatistic.Date <= end_date))
            result = await session.execute(stmt)
            return result.scalars().all()
