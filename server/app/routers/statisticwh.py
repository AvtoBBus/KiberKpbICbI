from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List
from app.schemas.statisticwh import StatisticWHDTO, StatisticWHDTO
from app.utils.db import get_db
from app.services.statisticwh import StatisticWHService
from app.services.user import UserService

router = APIRouter()

@router.get("/statisticwh", response_model=List[StatisticWHDTO])
def get_statisticwh(request: Request, db: Session = Depends(get_db)):
    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    service = StatisticWHService(db)
    stats = service.get_statisticwh(user.UserID)
    return [
        StatisticWHDTO(
            StatisticWHID=statisticwh.StatisticWHID,
            Date=statisticwh.Date,
            Height=statisticwh.Height,
            Weight=statisticwh.Weight
        ) for statisticwh in stats
    ]

@router.get("/statisticwh/{statisticwh_id}", response_model=StatisticWHDTO)
def get_statisticwh_id(request: Request, statisticwh_id: int, db: Session = Depends(get_db)):
    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    service = StatisticWHService(db)
    statisticwh = service.get_statisticwh_id(user.UserID, statisticwh_id)

    if not statisticwh:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Statistic about WH with id {statisticwh_id} doesn't exist"
        )

    return StatisticWHDTO(
        StatisticWHID=statisticwh.StatisticWHID,
        Date=statisticwh.Date,
        Height=statisticwh.Height,
        Weight=statisticwh.Weight
    )


@router.post("/statisticwh", response_model=StatisticWHDTO)
def add_statisticwh(request: Request, new_statisticwh: StatisticWHDTO, db: Session = Depends(get_db)):
    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    service = StatisticWHService(db)
    inserted = service.add_statisticwh(user.UserID, new_statisticwh)
    return StatisticWHDTO(
        StatisticWHID=inserted.StatisticWHID,
        Date=inserted.Date,
        Height=inserted.Height,
        Weight=inserted.Weight
    )