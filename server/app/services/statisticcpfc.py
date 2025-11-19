from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.statisticcpfc import StatisticCPFC
from app.schemas.statisticcpfc import StatisticCPFCDTO

from datetime import datetime


class StatisticCPFCService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_statisticcpfc_id(self, user_id: int, statisticcpfc_id: int):
        async with self.db as session:
            stmt = select(StatisticCPFC).where(and_(
                StatisticCPFC.UserID == user_id, StatisticCPFC.StatisticCPFCID == statisticcpfc_id))
            result = await session.execute(stmt)
            return result.scalars().first()

    async def get_statisticcpfc(self, user_id: int):
        async with self.db as session:
            stmt = select(StatisticCPFC).where(StatisticCPFC.UserID == user_id)
            result = await session.execute(stmt)
            return result.scalars().unique().all()

    async def get_statisticcpfc_by_date(self, user_id: int, start_date: datetime, end_date: datetime):
        async with self.db as session:
            stmt = select(StatisticCPFC).where(and_(StatisticCPFC.UserID == user_id,
                                                    StatisticCPFC.Date >= start_date, StatisticCPFC.Date <= end_date))
            result = await session.execute(stmt)
            return result.scalars().unique().all()

    async def add_statisticcpfc(self, user_id: int, new_statisticcpfc: StatisticCPFCDTO):
        async with self.db as session:
            inserted = StatisticCPFC(
                Date=new_statisticcpfc.Date,
                Calories=new_statisticcpfc.Calories,
                Protein=new_statisticcpfc.Protein,
                Fat=new_statisticcpfc.Fat,
                Carbonates=new_statisticcpfc.Carbonates,
                UserID=user_id
            )

            session.add(inserted)
            await session.commit()
            await session.refresh(inserted)

            return inserted

    async def edit_statisticcpfc(self, user_id: int, new_statisticcpfc: StatisticCPFCDTO):
        async with self.db as session:

            stmt = select(StatisticCPFC).where(and_(StatisticCPFC.UserID == user_id,
                                                    StatisticCPFC.StatisticCPFCID == new_statisticcpfc.StatisticCPFCID))
            result = await session.execute(stmt)

            findedStat = result.scalars().first()

            if not findedStat:
                raise ValueError

            findedStat.Date = new_statisticcpfc.Date
            findedStat.Calories = new_statisticcpfc.Calories
            findedStat.Protein = new_statisticcpfc.Protein
            findedStat.Fat = new_statisticcpfc.Fat
            findedStat.Carbonates = new_statisticcpfc.Carbonates

            await session.commit()
            await session.refresh(findedStat)

            return findedStat
