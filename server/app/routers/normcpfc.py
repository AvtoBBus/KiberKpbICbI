from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.normcpfc import NormCPFCResponse
from app.utils.db import get_db
from app.services.normcpfc import NormCPFCService

router = APIRouter()


@router.get("/normcpfc", response_model=List[NormCPFCResponse])
def get_food(db: Session = Depends(get_db)):
    service = NormCPFCService(db)
    norms = service.get_all_normcpfc()
    return [
        NormCPFCResponse(
            NormID=norm.NormID,
            MinHeight=norm.MinHeight,
            MaxHeight=norm.MaxHeight,
            MinWeight=norm.MinWeight,
            MaxWeight=norm.MaxWeight,
            Calories=norm.Calories,
            Protein=norm.Protein,
            Fats=norm.Fats,
            Carbonatest=norm.Carbonatest,
            Goal=norm.Goal.Name
        ) for norm in norms
    ]

@router.get("/normcpfc/{norm_id}", response_model=NormCPFCResponse)
def get_food(norm_id: int, db: Session = Depends(get_db)):
    service = NormCPFCService(db)
    norm = service.get_normcpfc(norm_id)
    return NormCPFCResponse(
        NormID=norm.NormID,
        MinHeight=norm.MinHeight,
        MaxHeight=norm.MaxHeight,
        MinWeight=norm.MinWeight,
        MaxWeight=norm.MaxWeight,
        Calories=norm.Calories,
        Protein=norm.Protein,
        Fats=norm.Fats,
        Carbonatest=norm.Carbonatest,
        Goal=norm.Goal.Name
    )