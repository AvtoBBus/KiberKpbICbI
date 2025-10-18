from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.statisticwh import StatisticWhResponse
from app.utils.db import get_db
from app.services.statisticwh import StatisticWhService

router = APIRouter()

@router.get("/statisticwh/{user_id}", response_model=List[StatisticWhResponse])
def get_statisticwh(user_id: int, db: Session = Depends(get_db)):
    service = StatisticWhService(db)
    stats = service.get_statisticwh(user_id)
    return [
        StatisticWhResponse(
            StatisticWHID=statisticwh.StatisticWHID,
            Date=statisticwh.Date,
            Height=statisticwh.Height,
            Weight=statisticwh.Weight
        ) for statisticwh in stats
    ]

@router.get("/statisticwh/{user_id}/{statisticwh_id}", response_model=StatisticWhResponse)
def get_statisticwh_id(user_id: int, statisticwh_id: int, db: Session = Depends(get_db)):
    service = StatisticWhService(db)
    statisticwh = service.get_statisticwh_id(user_id, statisticwh_id)
    return StatisticWhResponse(
        StatisticWHID=statisticwh.StatisticWHID,
        Date=statisticwh.Date,
        Height=statisticwh.Height,
        Weight=statisticwh.Weight
    )