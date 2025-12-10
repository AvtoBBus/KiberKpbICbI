from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.statisticcpfc import StatisticCPFC
from app.schemas.statisticcpfc import StatisticCPFCDTO

from datetime import datetime, timedelta


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

    async def get_statisticcpfc_by_date(self, user_id: int, start_date: datetime, end_date: datetime) -> list[StatisticCPFC]:
        async with self.db as session:
            stmt = select(StatisticCPFC).where(and_(StatisticCPFC.UserID == user_id,
                                                    StatisticCPFC.Date >= start_date, StatisticCPFC.Date <= end_date))
            result = await session.execute(stmt)
            existed = result.scalars().unique().all()

            count = end_date - start_date

            if count.days == 0:
                return existed

            result = []

            for i in range(0, count.days + 1):
                cur_date = start_date + timedelta(i)
                finded = None

                for e in existed:
                    if e.Date == cur_date:
                        finded = e
                        break

                if finded is not None:
                    result.append(finded)
                else:
                    result.append(StatisticCPFC(
                        StatisticCPFCID=-1 * (i + 1),
                        Date=cur_date,
                        Calories=0,
                        Protein=0,
                        Fats=0,
                        Carbonates=0,
                        UserID=user_id
                    )) 

            return result

    async def add_statisticcpfc(self, user_id: int, new_statisticcpfc: StatisticCPFCDTO):
        async with self.db as session:
            inserted = StatisticCPFC(
                Date=new_statisticcpfc.Date,
                Calories=new_statisticcpfc.Calories,
                Protein=new_statisticcpfc.Protein,
                Fats=new_statisticcpfc.Fats,
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
            findedStat.Fats = new_statisticcpfc.Fats
            findedStat.Carbonates = new_statisticcpfc.Carbonates

            await session.commit()
            await session.refresh(findedStat)

            return findedStat
