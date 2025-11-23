from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.userstatistic import UserStatisticDTO
from app.utils.db import get_db
from app.services.userstatistic import UserStatisticService
from app.services.user import UserService
from app.utils.security import Security

from typing import List, Annotated
from datetime import datetime

router = APIRouter()
oauth2_scheme = APIKeyHeader(name="token")

@router.get("/userstatistic", response_model=List[UserStatisticDTO])
async def get_userstatistic(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_db)
):

    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    service = UserStatisticService(db)
    stats = await service.get_userstatistic(user.UserID)
    return [
        UserStatisticDTO(
            UserID=userstatistic.UserID,
            Date= userstatistic.Date,
            UserHeight= userstatistic.UserHeight,
            UserWeight=userstatistic.UserWeight,
            Calories=userstatistic.Calories,
            Protein=userstatistic.Protein,
            Fat=userstatistic.Fat,
            Carbonates=userstatistic.Carbonates,
        ) for userstatistic in stats
    ]

@router.get("/userstatistic/fromTo", response_model=List[UserStatisticDTO])
async def get_userstatistic_by_date(
    token: Annotated[str, Depends(oauth2_scheme)],
    start_date: datetime,
    end_date: datetime,
    db: AsyncSession = Depends(get_db)
):
    print(1)
    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        print(2)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    print(3)
    if start_date > end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="StartDate must by below or equal EndDate"
        )

    service = UserStatisticService(db)
    stats = await service.get_userstatistic_by_date(user.UserID, start_date, end_date)
    print(4)
    return [
        UserStatisticDTO(
            UserID=userstatistic.UserID,
            Date= userstatistic.Date,
            UserHeight= userstatistic.UserHeight,
            UserWeight=userstatistic.UserWeight,
            Calories=userstatistic.Calories,
            Protein=userstatistic.Protein,
            Fat=userstatistic.Fat,
            Carbonates=userstatistic.Carbonates,
        ) for userstatistic in stats
    ]