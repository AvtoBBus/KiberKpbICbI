from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.normcpfc import NormCPFC
from app.schemas.normcpfc import NormCPFCDTO

class NormCPFCService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_normcpfc(self, user_id: int):
        async with self.db as session:
            stmt = select(NormCPFC).where(NormCPFC.UserID == user_id)
            result = await session.execute(stmt)
            return result.scalars().first()

    async def add_normcpfc(self, user_id: int, new_norm: NormCPFCDTO):
        async with self.db as session:
            stmt = select(NormCPFC).where(NormCPFC.UserID == user_id)
            result = await session.execute(stmt)

            checkExist = result.scalars().first()

            if checkExist is not None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="NormCPFC for user already exist"
                )

            inserted = NormCPFC(
                MinHeight=new_norm.MinHeight,
                MaxHeight=new_norm.MaxHeight,
                MinWeight=new_norm.MinWeight,
                MaxWeight=new_norm.MaxWeight,
                Calories=new_norm.Calories,
                Protein=new_norm.Protein,
                Fats=new_norm.Fats,
                Carbonatest=new_norm.Carbonatest,
                UserID=user_id
            )

            session.add(inserted)
            await session.commit()
            await session.refresh(inserted)

            return inserted

    async def edit_normcpfc(self, user_id: int, new_norm: NormCPFCDTO):
        async with self.db as session:
            stmt = select(NormCPFC).where(NormCPFC.UserID == user_id)
            result = await session.execute(stmt)

            findedNorm = result.scalars().first()

            if not findedNorm or not findedNorm.NormID.__eq__(new_norm.NormID):
                raise ValueError

            findedNorm.MinHeight=new_norm.MinHeight
            findedNorm.MaxHeight=new_norm.MaxHeight
            findedNorm.MinWeight=new_norm.MinWeight
            findedNorm.MaxWeight=new_norm.MaxWeight
            findedNorm.Calories=new_norm.Calories
            findedNorm.Protein=new_norm.Protein
            findedNorm.Fats=new_norm.Fats
            findedNorm.Carbonatest=new_norm.Carbonatest

            await session.commit()
            await session.refresh(findedNorm)

            return findedNorm
