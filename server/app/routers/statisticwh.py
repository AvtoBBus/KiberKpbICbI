from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.statisticwh import StatisticWHDTO, StatisticWHDTO
from app.utils.db import get_db
from app.services.statisticwh import StatisticWHService
from app.services.user import UserService
from app.utils.security import Security

from typing import List, Annotated
from datetime import datetime

router = APIRouter()
oauth2_scheme = APIKeyHeader(name="token")

@router.get("/statisticwh", response_model=List[StatisticWHDTO])
async def get_statisticwh(
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
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )

    service = StatisticWHService(db)
    stats = await service.get_statisticwh(user.UserID)
    return [
        StatisticWHDTO(
            StatisticWHID=statisticwh.StatisticWHID,
            Date=statisticwh.Date,
            Height=statisticwh.Height,
            Weight=statisticwh.Weight
        ) for statisticwh in stats
    ]

@router.get("/statisticwh/fromTo", response_model=List[StatisticWHDTO])
async def get_statisticwh_by_date(
    token: Annotated[str, Depends(oauth2_scheme)],
    start_date: datetime,
    end_date: datetime,
    db: AsyncSession = Depends(get_db)
):
    auth = UserService(db)
    security = Security(db)

    try:
        user = await auth.get_user(token)
        if not await security.check_user_token(token, user.UserID):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )

    if start_date > end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={ "message": "Дата начала должна быть раньше или равна дате конца" }
        )

    service = StatisticWHService(db)
    stats = await service.get_statisticwh_by_date(user.UserID, start_date, end_date)
    return [
        StatisticWHDTO(
            StatisticWHID=statisticwh.StatisticWHID,
            Date=statisticwh.Date,
            Height=statisticwh.Height,
            Weight=statisticwh.Weight
        ) for statisticwh in stats
    ]

@router.get("/statisticwh/{statisticwh_id}", response_model=StatisticWHDTO)
async def get_statisticwh_id(
    statisticwh_id: int,
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
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )
    
    service = StatisticWHService(db)
    statisticwh = await service.get_statisticwh_id(user.UserID, statisticwh_id)

    if not statisticwh:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={ "message": f"Не удалось найти статистику по КБЖУ с id {statisticwh_id}" }
        )

    return StatisticWHDTO(
        StatisticWHID=statisticwh.StatisticWHID,
        Date=statisticwh.Date,
        Height=statisticwh.Height,
        Weight=statisticwh.Weight
    )


@router.post("/statisticwh", response_model=StatisticWHDTO)
async def add_statisticwh(
    new_statisticwh: StatisticWHDTO,
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
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )
    
    service = StatisticWHService(db)
    inserted = await service.add_statisticwh(user.UserID, new_statisticwh)
    return StatisticWHDTO(
        StatisticWHID=inserted.StatisticWHID,
        Date=inserted.Date,
        Height=inserted.Height,
        Weight=inserted.Weight
    )

@router.put("/statisticwh", response_model=StatisticWHDTO)
async def edit_statisticwh(
    new_statisticwh: StatisticWHDTO,
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
                detail={ "message": "Неверный токен" },
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Неверный токен" },
        )
    
    service = StatisticWHService(db)
    try:
        updated = await service.edit_statisticwh(user.UserID, new_statisticwh)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={ "message": f"Не удалось найти статистику по КБЖУ с id {new_statisticwh.StatisticWHID}" }
        )
    
    return updated