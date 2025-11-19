from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.userdata import UserData
from app.schemas.userdata import UserDataDTO


class UserDataService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_userdata(self, user_id: int):
        async with self.db as session:
            stmt = select(UserData).where(UserData.UserID == user_id)
            result = await session.execute(stmt)
            data = result.scalars().first()
            return data

    async def add_userdata(self, user_id: int, new_userdata: UserDataDTO):
        async with self.db as session:

            stmt = select(UserData).where(UserData.UserID == user_id)
            result = await session.execute(stmt)
            checkExist = result.scalars().first()

            if checkExist is not None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="UserData for user already exist"
                )

            inserted = UserData(
                UserName = new_userdata.UserName,
                Height = new_userdata.Height,
                Weight = new_userdata.Weight,
                DesiredHeight = new_userdata.DesiredHeight,
                DesiredWeight = new_userdata.DesiredWeight,
                Activity  = new_userdata.Activity,
                Age = new_userdata.Age,
                UserID = user_id
            )

            session.add(inserted)
            await session.commit()
            await session.refresh(inserted)

            return inserted
    
    async def edit_userdata(self, user_id: int, new_userdata: UserDataDTO):
        async with self.db as session:
            stmt = select(UserData).where(UserData.UserID == user_id)
            result = await session.execute(stmt)
        
            findedUData = result.scalars().first()

            if not findedUData or not findedUData.UserDataID.__eq__(new_userdata.UserDataID):
                raise ValueError

            findedUData.UserName = new_userdata.UserName
            findedUData.Height = new_userdata.Height
            findedUData.Weight = new_userdata.Weight
            findedUData.DesiredHeight = new_userdata.DesiredHeight
            findedUData.DesiredWeight = new_userdata.DesiredWeight
            findedUData.Activity = new_userdata.Activity
            findedUData.Age = new_userdata.Age

            await session.commit()
            await session.refresh(findedUData)

            return findedUData