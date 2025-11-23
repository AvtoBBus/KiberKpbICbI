from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile, Request
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils.db import get_db
from app.utils.security import Security
from app.services.user import UserService
from app.utils.askAI import describe_image

from typing import Annotated


router = APIRouter()

oauth2_scheme = APIKeyHeader(name="token")

@router.post("/image")
async def send_image(
    request: Request,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_db),
    file: UploadFile = File(...),
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
    
    contents = await file.read()
    result = await describe_image(contents, file, request.client.host)
    return result   