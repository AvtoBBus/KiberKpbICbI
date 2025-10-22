from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.statisticwh import StatisticWHDTO, StatisticWHDTO
from app.utils.db import get_db
from app.services.statisticwh import StatisticWHService

router = APIRouter()

@router.get("/statisticwh/{user_id}", response_model=List[StatisticWHDTO])
def get_statisticwh(user_id: int, db: Session = Depends(get_db)):
    service = StatisticWHService(db)
    stats = service.get_statisticwh(user_id)
    return [
        StatisticWHDTO(
            StatisticWHID=statisticwh.StatisticWHID,
            Date=statisticwh.Date,
            Height=statisticwh.Height,
            Weight=statisticwh.Weight
        ) for statisticwh in stats
    ]

@router.get("/statisticwh/{user_id}/{statisticwh_id}", response_model=StatisticWHDTO)
def get_statisticwh_id(user_id: int, statisticwh_id: int, db: Session = Depends(get_db)):
    service = StatisticWHService(db)
    statisticwh = service.get_statisticwh_id(user_id, statisticwh_id)
    return StatisticWHDTO(
        StatisticWHID=statisticwh.StatisticWHID,
        Date=statisticwh.Date,
        Height=statisticwh.Height,
        Weight=statisticwh.Weight
    )


@router.post("/statisticwh/{user_id}", response_model=StatisticWHDTO)
def get_statisticwh_id(user_id: int, new_statisticwh: StatisticWHDTO, db: Session = Depends(get_db)):
    service = StatisticWHService(db)
    inserted = service.add_statisticwh(user_id, new_statisticwh)
    return StatisticWHDTO(
        StatisticWHID=inserted.StatisticWHID,
        Date=inserted.Date,
        Height=inserted.Height,
        Weight=inserted.Weight
    )