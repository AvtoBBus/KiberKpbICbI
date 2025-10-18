from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import config

from app.routers import food as food_router
from app.routers import normcpfc as normcpfc_router
from app.routers import userdata as userdata_router
from app.routers import user as user_router
from app.routers import statisticwh as statisticwh_router

app = FastAPI(
    swagger_ui_parameters={ "syntaxHighlight": True }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(food_router.router, prefix=config.settings.API_STR, tags=["Получение списка продуктов"])
app.include_router(normcpfc_router.router, prefix=config.settings.API_STR, tags=["Получение норм"])
app.include_router(userdata_router.router, prefix=config.settings.API_STR, tags=["Получение данных пользователя"])
app.include_router(user_router.router, prefix=config.settings.API_STR, tags=["Получение пользователя"])
app.include_router(statisticwh_router.router, prefix=config.settings.API_STR, tags=["Получение статистики пользователя"])