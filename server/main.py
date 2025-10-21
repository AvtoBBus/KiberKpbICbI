from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import config

from app.routers import food as food_router
from app.routers import meal as meal_router

from app.routers import normcpfc as normcpfc_router
from app.routers import userdata as userdata_router
from app.routers import user as user_router

from app.routers import statisticwh as statisticwh_router
from app.routers import statisticcpfc as statisticcpfc_router
from app.routers import userstatistic as userstatistic_router

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

app.include_router(food_router.router, prefix=config.settings.api_strings['General'], tags=["Продукты"])

app.include_router(normcpfc_router.router, prefix=config.settings.api_strings['User']["Data"], tags=["Нормы КБЖУ пользователя"])
app.include_router(userdata_router.router, prefix=config.settings.api_strings['User']["Data"], tags=["Данные пользователя"])
app.include_router(user_router.router, prefix=config.settings.api_strings['User']["Data"], tags=["Получение пользователя"])
app.include_router(meal_router.router, prefix=config.settings.api_strings['User']["Data"], tags=["Приемы пищи пользователя"])

app.include_router(statisticwh_router.router, prefix=config.settings.api_strings['User']["Statistic"], tags=["Статистика по росту/весу"])
app.include_router(statisticcpfc_router.router, prefix=config.settings.api_strings['User']["Statistic"], tags=["Статистика по КБЖУ"])
app.include_router(userstatistic_router.router, prefix=config.settings.api_strings['User']["Statistic"], tags=["Статистика пользователя"])