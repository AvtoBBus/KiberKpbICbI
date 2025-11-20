from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.normcpfc import NormCPFC
from app.schemas.normcpfc import NormCPFCDTO, NormCPFCDTOPost

from app.utils.calculatorCPFC import calculatorCPFC

class NormCPFCService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_normcpfc(self, user_id: int):
        async with self.db as session:
            stmt = select(NormCPFC).where(NormCPFC.UserID == user_id)
            result = await session.execute(stmt)
            return result.scalars().first()

    async def add_normcpfc(self, user_id: int, new_norm: NormCPFCDTOPost):
        async with self.db as session:
            stmt = select(NormCPFC).where(NormCPFC.UserID == user_id)
            result = await session.execute(stmt)

            checkExist = result.scalars().first()

            if checkExist is not None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="NormCPFC for user already exist"
                )
            
            calc = calculatorCPFC(
                weight=new_norm.Weight,
                height=new_norm.Height,
                desired_weight=new_norm.DesiredWeight,
                age=new_norm.Age,
                gender=new_norm.Gender,
                activity=new_norm.Activity
            )

            result_calc = calc.calculate_for_target_weight()['current']

            inserted = NormCPFC(
                Weight=new_norm.Weight,
                Height=new_norm.Height,
                DesiredWeight=new_norm.DesiredWeight,
                Calories=result_calc['calorie_goal'],
                Protein=result_calc['macros']['protein'],
                Fats=result_calc['macros']['fat'],
                Carbonatest=result_calc['macros']['carbs'],
                UserID=user_id
            )

            session.add(inserted)
            await session.commit()
            await session.refresh(inserted)

            return inserted

    async def edit_normcpfc(self, user_id: int, new_norm: NormCPFCDTOPost):
        async with self.db as session:
            stmt = select(NormCPFC).where(NormCPFC.UserID == user_id)
            result = await session.execute(stmt)

            findedNorm = result.scalars().first()

            calc = calculatorCPFC(
                weight=new_norm.Weight,
                height=new_norm.Height,
                desired_weight=new_norm.DesiredWeight,
                age=new_norm.Age,
                gender=new_norm.Gender,
                activity=new_norm.Activity
            )

            result_calc = calc.calculate_for_target_weight()['target']

            findedNorm.Height=new_norm.Height,
            findedNorm.Weight=new_norm.Weight,
            findedNorm.DesiredWeight=new_norm.DesiredWeight,
            findedNorm.Calories=result_calc['calorie_goal']
            findedNorm.Protein=result_calc['macros']['protein']
            findedNorm.Fats=result_calc['macros']['fat']
            findedNorm.Carbonatest=result_calc['macros']['carbs']

            await session.commit()
            await session.refresh(findedNorm)

            return findedNorm
