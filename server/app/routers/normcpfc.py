from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from app.schemas.normcpfc import NormCPFCDTO, NormCPFCDTO
from app.services.normcpfc import NormCPFCService
from app.services.user import UserService
from app.utils.security import Security
from app.utils.db import get_db

from typing import List, Annotated

router = APIRouter()
oauth2_scheme = APIKeyHeader(name="token")

@router.get("/normcpfc", response_model=List[NormCPFCDTO])
def get_normcpfc(
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

    service = NormCPFCService(db)
    norms = service.get_normcpfc(user.UserID)
    return [
        NormCPFCDTO(
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

@router.get("/normcpfc/{norm_id}", response_model=NormCPFCDTO)
def get_normcpfc_id(
    norm_id: int, 
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
    
    service = NormCPFCService(db)
    norm = service.get_normcpfc_id(user.UserID, norm_id)

    if not norm:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Norm with id {norm_id} doesn't exist"
        )

    return NormCPFCDTO(
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

@router.post("/normcpfc", response_model=NormCPFCDTO)
def add_normcpfc(
    new_norm: NormCPFCDTO,
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

    service = NormCPFCService(db)
    inserted = service.add_normcpfc(user.UserID, new_norm)
    
    return NormCPFCDTO(
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

@router.put("/normcpfc", response_model=NormCPFCDTO)
def edit_normcpfc(
    new_norm: NormCPFCDTO,
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

    service = NormCPFCService(db)

    try:
        updated = service.edit_normcpfc(user.UserID, new_norm)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Norm with id {new_norm.NormID} doesn't exist"
        )
    
    return updated