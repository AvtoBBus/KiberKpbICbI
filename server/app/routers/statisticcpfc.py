from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.statisticcpfc import StatisticCPFCDTO, StatisticCPFCDTO
from app.services.statisticcpfc import StatisticCPFCService
from app.services.user import UserService
from app.utils.security import Security
from app.utils.db import get_db

from typing import List, Annotated
from datetime import datetime

router = APIRouter()
oauth2_scheme = APIKeyHeader(name="token")

@router.get("/statisticcpfc", response_model=List[StatisticCPFCDTO])
async def get_statisticcpfc(
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

    service = StatisticCPFCService(db)
    stats = await service.get_statisticcpfc(user.UserID)
    return [
        StatisticCPFCDTO(
            StatisticCPFCID=statisticcpfc.StatisticCPFCID,
            Date=statisticcpfc.Date,
            Calories=statisticcpfc.Calories,
            Protein=statisticcpfc.Protein,
            Fats=statisticcpfc.Fats,
            Carbonates=statisticcpfc.Carbonates
        ) for statisticcpfc in stats
    ]

@router.get("/statisticcpfc/fromTo", response_model=List[StatisticCPFCDTO])
async def get_statisticcpfc_by_date(
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
                detail="Incorrect token",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    if start_date > end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="StartDate must by below or equal EndDate"
        )

    service = StatisticCPFCService(db)
    stats = await service.get_statisticcpfc_by_date(user.UserID, start_date, end_date)
    return [
        StatisticCPFCDTO(
            StatisticCPFCID=statisticcpfc.StatisticCPFCID,
            Date=statisticcpfc.Date,
            Calories=statisticcpfc.Calories,
            Protein=statisticcpfc.Protein,
            Fats=statisticcpfc.Fats,
            Carbonates=statisticcpfc.Carbonates
        ) for statisticcpfc in stats
    ]

@router.get("/statisticcpfc/{statisticcpfc_id}", response_model=StatisticCPFCDTO)
async def get_statisticcpfc_id(
    statisticcpfc_id: int,
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
    
    service = StatisticCPFCService(db)
    statisticcpfc = await service.get_statisticwh_id(user.UserID, statisticcpfc_id)

    if not statisticcpfc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Statistic about CPFC with id {statisticcpfc_id} doesn't exist"
        )
    
    return StatisticCPFCDTO(
        StatisticCPFCID=statisticcpfc.StatisticCPFCID,
        Date=statisticcpfc.Date,
        Calories=statisticcpfc.Calories,
        Protein=statisticcpfc.Protein,
        Fats=statisticcpfc.Fats,
        Carbonates=statisticcpfc.Carbonates
    )

@router.post("/statisticcpfc", response_model=StatisticCPFCDTO)
async def add_statisticwh(
    new_statisticcpfc: StatisticCPFCDTO,
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
    
    service = StatisticCPFCService(db)
    inserted = await service.add_statisticcpfc(user.UserID, new_statisticcpfc)
    return StatisticCPFCDTO(
        StatisticCPFCID=inserted.StatisticCPFCID,
        Date=inserted.Date,
        Calories=inserted.Calories,
        Protein=inserted.Protein,
        Fats=inserted.Fats,
        Carbonates=inserted.Carbonates
    )

@router.put("/statisticcpfc", response_model=StatisticCPFCDTO)
async def edit_statisticwh(
    new_statisticcpfc: StatisticCPFCDTO,
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
    
    service = StatisticCPFCService(db)
    try:
        updated = await service.edit_statisticcpfc(user.UserID, new_statisticcpfc)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Statistic about CPFC with id {new_statisticcpfc.StatisticCPFCID} doesn't exist"
        )
    
    return updated