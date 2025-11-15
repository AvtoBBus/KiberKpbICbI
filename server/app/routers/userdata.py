from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from app.schemas.userdata import UserDataDTO, UserDataDTO
from app.utils.db import get_db
from app.services.userdata import UserDataService
from app.services.user import UserService
from app.utils.security import Security

from typing import List, Annotated

router = APIRouter()
oauth2_scheme = APIKeyHeader(name="token")


@router.get("/userdata", response_model=List[UserDataDTO])
def get_userdata(
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

    service = UserDataService(db)
    data = service.get_userdata(user.UserID)

    return [
        UserDataDTO(
            UserDataID=userData.UserDataID,
            Height=userData.Height,
            Weight=userData.Weight,
            DesiredHeight=userData.DesiredHeight,
            DesiredWeight=userData.DesiredWeight,
            Activity=userData.Activity,
            Age=userData.Age,
        ) for userData in data
    ]


@router.get("/userdata/{user_data_id}", response_model=UserDataDTO)
def get_userdata_id(
    user_data_id: int,
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
    
    service = UserDataService(db)
    userData = service.get_userdata_id(user.UserID, user_data_id)        

    if not userData:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Userdata with id {user_data_id} doesn't exist"
        )

    return UserDataDTO(
        UserDataID=userData.UserDataID,
        Height=userData.Height,
        Weight=userData.Weight,
        DesiredHeight=userData.DesiredHeight,
        DesiredWeight=userData.DesiredWeight,
        Activity=userData.Activity,
        Age=userData.Age,
    )


@router.post("/userdata", response_model=UserDataDTO)
def add_userdata(
    new_user_data: UserDataDTO,
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
    
    service = UserDataService(db)
    inserted = service.add_userdata(user.UserID, new_user_data)
    return UserDataDTO(
        UserDataID=inserted.UserDataID,
        Height=inserted.Height,
        Weight=inserted.Weight,
        DesiredHeight=inserted.DesiredHeight,
        DesiredWeight=inserted.DesiredWeight,
        Activity=inserted.Activity,
        Age=inserted.Age,
    )

@router.put("/userdata", response_model=UserDataDTO)
def edit_userdata(
    new_user_data: UserDataDTO,
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
    
    service = UserDataService(db)
    try:
        updated = service.edit_userdata(user.UserID, new_user_data)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User data with id {new_user_data.UserDataID} doesn't exist"
        )
    
    return updated

