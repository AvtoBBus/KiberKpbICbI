from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List
from app.schemas.statisticcpfc import StatisticCPFCDTO, StatisticCPFCDTO
from app.utils.db import get_db
from app.services.statisticcpfc import StatisticCPFCService
from app.services.user import UserService

router = APIRouter()

@router.get("/statisticcpfc", response_model=List[StatisticCPFCDTO])
def get_statisticcpfc(request: Request, db: Session = Depends(get_db)):

    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )

    service = StatisticCPFCService(db)
    stats = service.get_statisticwh(user.UserID)
    return [
        StatisticCPFCDTO(
            StatisticCPFCID=statisticcpfc.StatisticCPFCID,
            Date=statisticcpfc.Date,
            Calories=statisticcpfc.Calories,
            Protein=statisticcpfc.Protein,
            Fat=statisticcpfc.Fat,
            Carbonates=statisticcpfc.Carbonates
        ) for statisticcpfc in stats
    ]

@router.get("/statisticcpfc/{statisticcpfc_id}", response_model=StatisticCPFCDTO)
def get_statisticcpfc_id(request: Request, statisticcpfc_id: int, db: Session = Depends(get_db)):

    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    service = StatisticCPFCService(db)
    statisticcpfc = service.get_statisticwh_id(user.UserID, statisticcpfc_id)

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
        Fat=statisticcpfc.Fat,
        Carbonates=statisticcpfc.Carbonates
    )

@router.post("/statisticcpfc", response_model=StatisticCPFCDTO)
def add_statisticwh(request: Request, new_statisticcpfc: StatisticCPFCDTO, db: Session = Depends(get_db)):

    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    service = StatisticCPFCService(db)
    inserted = service.add_statisticcpfc(user.UserID, new_statisticcpfc)
    return StatisticCPFCDTO(
        StatisticCPFCID=inserted.StatisticCPFCID,
        Date=inserted.Date,
        Calories=inserted.Calories,
        Protein=inserted.Protein,
        Fat=inserted.Fat,
        Carbonates=inserted.Carbonates
    )

@router.put("/statisticcpfc", response_model=StatisticCPFCDTO)
def edit_statisticwh(request: Request, new_statisticcpfc: StatisticCPFCDTO, db: Session = Depends(get_db)):

    auth = UserService(db)
    try:
        token = request.cookies.get("token")
        user = auth.get_user(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    
    service = StatisticCPFCService(db)
    try:
        updated = service.edit_statisticcpfc(user.UserID, new_statisticcpfc)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Statistic about CPFC with id {new_statisticcpfc.StatisticCPFCID} doesn't exist"
        )
    
    return updated