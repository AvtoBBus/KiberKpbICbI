from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.normcpfc import NormCPFCDTO, NormCPFCDTO, NormCPFCDTOPost
from app.services.normcpfc import NormCPFCService
from app.services.user import UserService
from app.utils.security import Security
from app.utils.db import get_db

from typing import Optional, Annotated

router = APIRouter()
oauth2_scheme = APIKeyHeader(name="token")

@router.get("/normcpfc", response_model=Optional[NormCPFCDTO])
async def get_normcpfc(
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

    service = NormCPFCService(db)
    norm = await service.get_normcpfc(user.UserID)

    if norm is None:
        return None

    return NormCPFCDTO(
            NormID=norm.NormID,
            Height=norm.Height,
            Weight=norm.Weight,
            DesiredWeight=norm.DesiredWeight,
            Calories=norm.Calories,
            Protein=norm.Protein,
            Fats=norm.Fats,
            Carbonatest=norm.Carbonatest,
        )

@router.post("/normcpfc", response_model=NormCPFCDTO)
async def add_normcpfc(
    new_norm: NormCPFCDTOPost,
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

    service = NormCPFCService(db)
    inserted = await service.add_normcpfc(user.UserID, new_norm)
    
    return NormCPFCDTO(
        NormID=inserted.NormID,
        Height=inserted.Height,
        Weight=inserted.Weight,
        DesiredWeight=inserted.DesiredWeight,
        Calories=inserted.Calories,
        Protein=inserted.Protein,
        Fats=inserted.Fats,
        Carbonatest=inserted.Carbonatest,
    )

@router.put("/normcpfc", response_model=NormCPFCDTO)
async def edit_normcpfc(
    new_norm: NormCPFCDTOPost,
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

    service = NormCPFCService(db)

    try:
        updated = await service.edit_normcpfc(user.UserID, new_norm)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Norm with id {new_norm.NormID} doesn't exist"
        )
    
    return updated