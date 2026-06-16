from app.models.statisticwh import StatisticWH
from app.schemas.statisticwh import StatisticWHDTO

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from datetime import datetime

class StatisticWHService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_statisticwh_id(self, user_id: int, statisticwh_id: int):
        async with self.db as session:
            stmt = select(StatisticWH).where(and_(StatisticWH.UserID == user_id, StatisticWH.StatisticWHID == statisticwh_id))
            result = await session.execute(stmt)
            return result.scalars().first()

    async def get_statisticwh(self, user_id: int):
        async with self.db as session:
            stmt = select(StatisticWH).where(StatisticWH.UserID == user_id)
            result = await session.execute(stmt)
            return result.scalars().all()
    
    async def get_statisticwh_by_date(self, user_id: int, start_date: datetime, end_date: datetime):
        async with self.db as session:
            stmt = select(StatisticWH).where(and_(StatisticWH.UserID == user_id,
                                                    StatisticWH.Date >= start_date, StatisticWH.Date <= end_date))
            result = await session.execute(stmt)
            return result.scalars().unique().all()

    async def add_statisticwh(self, user_id: int, new_statisticwh: StatisticWHDTO):
        async with self.db as session:

            inserted = StatisticWH(
                Date = new_statisticwh.Date,
                Height = new_statisticwh.Height,
                Weight = new_statisticwh.Weight,
                UserID = user_id
            )

            session.add(inserted)
            await session.commit()
            await session.refresh(inserted)

            return inserted
    
    async def edit_statisticwh(self, user_id: int, new_statisticwh: StatisticWHDTO):
        async with self.db as session:
            stmt = select(StatisticWH).where(and_(StatisticWH.UserID == user_id, StatisticWH.StatisticWHID == new_statisticwh.StatisticWHID))
            result = await session.execute(stmt)

            findedStat = result.scalars().first()

            if not findedStat:
                raise ValueError

            findedStat.Date = new_statisticwh.Date
            findedStat.Height = new_statisticwh.Height
            findedStat.Weight = new_statisticwh.Weight

            await session.commit()
            await session.refresh(findedStat)

            return findedStat