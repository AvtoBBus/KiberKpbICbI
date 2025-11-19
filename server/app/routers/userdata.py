from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.userdata import UserDataDTO, UserDataDTO
from app.utils.db import get_db
from app.services.userdata import UserDataService
from app.services.user import UserService
from app.utils.security import Security

from typing import Optional, Annotated

router = APIRouter()
oauth2_scheme = APIKeyHeader(name="token")


@router.get("/userdata", response_model=Optional[UserDataDTO])
async def get_userdata(
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

    service = UserDataService(db)
    userData = await service.get_userdata(user.UserID)

    if userData is None:
        return None

    return UserDataDTO(
            UserDataID=userData.UserDataID,
            UserName=userData.UserName,
            Height=userData.Height,
            Weight=userData.Weight,
            DesiredHeight=userData.DesiredHeight,
            DesiredWeight=userData.DesiredWeight,
            Activity=userData.Activity,
            Age=userData.Age,
            Gender=userData.Gender,
        )

@router.post("/userdata", response_model=UserDataDTO)
async def add_userdata(
    new_user_data: UserDataDTO,
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
    
    service = UserDataService(db)
    inserted = await service.add_userdata(user.UserID, new_user_data)
    return UserDataDTO(
        UserDataID=inserted.UserDataID,
        UserName=inserted.UserName,
        Height=inserted.Height,
        Weight=inserted.Weight,
        DesiredHeight=inserted.DesiredHeight,
        DesiredWeight=inserted.DesiredWeight,
        Activity=inserted.Activity,
        Age=inserted.Age,
        Gender=inserted.Gender,
    )

@router.put("/userdata", response_model=UserDataDTO)
async def edit_userdata(
    new_user_data: UserDataDTO,
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
    
    service = UserDataService(db)
    try:
        updated = await service.edit_userdata(user.UserID, new_user_data)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User data with id {new_user_data.UserDataID} doesn't exist"
        )
    
    return updated