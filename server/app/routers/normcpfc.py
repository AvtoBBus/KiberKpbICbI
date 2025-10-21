from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.normcpfc import NormCPFCResponse, NormCPFCRequest
from app.utils.db import get_db
from app.services.normcpfc import NormCPFCService

router = APIRouter()


@router.get("/normcpfc/{user_id}", response_model=List[NormCPFCResponse])
def get_normcpfc(user_id: int, db: Session = Depends(get_db)):
    service = NormCPFCService(db)
    norms = service.get_normcpfc(user_id)
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
        ) for norm in norms
    ]

@router.get("/normcpfc/{user_id}/{norm_id}", response_model=NormCPFCResponse)
def get_normcpfc_id(user_id: int, norm_id: int, db: Session = Depends(get_db)):
    service = NormCPFCService(db)
    norm = service.get_normcpfc_id(user_id, norm_id)
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
    )

@router.post("/normcpfc/{user_id}", response_model=NormCPFCResponse)
def get_normcpfc_id(user_id: int, new_norm: NormCPFCRequest, db: Session = Depends(get_db)):
    service = NormCPFCService(db)
    inserted = service.add_normcpfc(user_id, new_norm)
    return NormCPFCResponse(
        NormID=inserted.NormID,
        MinHeight=inserted.MinHeight,
        MaxHeight=inserted.MaxHeight,
        MinWeight=inserted.MinWeight,
        MaxWeight=inserted.MaxWeight,
        Calories=inserted.Calories,
        Protein=inserted.Protein,
        Fats=inserted.Fats,
        Carbonatest=inserted.Carbonatest,
    )