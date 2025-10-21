from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.statisticcpfc import StatisticCPFCResponse, StatisticCPFCRequest
from app.utils.db import get_db
from app.services.statisticcpfc import StatisticCPFCService

router = APIRouter()

@router.get("/statisticcpfc/{user_id}", response_model=List[StatisticCPFCResponse])
def get_statisticcpfc(user_id: int, db: Session = Depends(get_db)):
    service = StatisticCPFCService(db)
    stats = service.get_statisticwh(user_id)
    return [
        StatisticCPFCResponse(
            StatisticCPFCID=statisticcpfc.StatisticCPFCID,
            Date=statisticcpfc.Date,
            Calories=statisticcpfc.Calories,
            Protein=statisticcpfc.Protein,
            Fat=statisticcpfc.Fat,
            Carbonates=statisticcpfc.Carbonates
        ) for statisticcpfc in stats
    ]

@router.get("/statisticcpfc/{user_id}/{statisticcpfc_id}", response_model=StatisticCPFCResponse)
def get_statisticcpfc_id(user_id: int, statisticcpfc_id: int, db: Session = Depends(get_db)):
    service = StatisticCPFCService(db)
    statisticcpfc = service.get_statisticwh_id(user_id, statisticcpfc_id)
    return StatisticCPFCResponse(
        StatisticCPFCID=statisticcpfc.StatisticCPFCID,
        Date=statisticcpfc.Date,
        Calories=statisticcpfc.Calories,
        Protein=statisticcpfc.Protein,
        Fat=statisticcpfc.Fat,
        Carbonates=statisticcpfc.Carbonates
    )

@router.post("/statisticcpfc/{user_id}", response_model=StatisticCPFCResponse)
def get_statisticwh_id(user_id: int, new_statisticcpfc: StatisticCPFCRequest, db: Session = Depends(get_db)):
    service = StatisticCPFCService(db)
    inserted = service.add_statisticcpfc(user_id, new_statisticcpfc)
    return StatisticCPFCResponse(
        StatisticCPFCID=inserted.StatisticCPFCID,
        Date=inserted.Date,
        Calories=inserted.Calories,
        Protein=inserted.Protein,
        Fat=inserted.Fat,
        Carbonates=inserted.Carbonates
    )