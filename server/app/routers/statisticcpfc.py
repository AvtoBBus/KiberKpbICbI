from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from app.schemas.statisticcpfc import StatisticCPFCDTO, StatisticCPFCDTO
from app.services.statisticcpfc import StatisticCPFCService
from app.services.user import UserService
from app.utils.security import Security
from app.utils.db import get_db

from typing import List, Annotated

router = APIRouter()
oauth2_scheme = APIKeyHeader(name="token")

@router.get("/statisticcpfc", response_model=List[StatisticCPFCDTO])
def get_statisticcpfc(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):

    auth = UserService(db)
    security = Security(db)
    
    try:
        user = auth.get_user(token)
        if not security.check_user_token(token, user.UserID):
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
def get_statisticcpfc_id(
    statisticcpfc_id: int,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):

    auth = UserService(db)
    security = Security(db)
    
    try:
        user = auth.get_user(token)
        if not security.check_user_token(token, user.UserID):
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
def add_statisticwh(
    new_statisticcpfc: StatisticCPFCDTO,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):

    auth = UserService(db)
    security = Security(db)
    
    try:
        user = auth.get_user(token)
        if not security.check_user_token(token, user.UserID):
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
def edit_statisticwh(
    new_statisticcpfc: StatisticCPFCDTO,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):

    auth = UserService(db)
    security = Security(db)
    
    try:
        user = auth.get_user(token)
        if not security.check_user_token(token, user.UserID):
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
        updated = service.edit_statisticcpfc(user.UserID, new_statisticcpfc)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Statistic about CPFC with id {new_statisticcpfc.StatisticCPFCID} doesn't exist"
        )
    
    return updated