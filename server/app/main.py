from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import config
from app.routers import food as food_router

app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight": True}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(food_router.router, prefix=config.settings.API_STR, tags=["food"])