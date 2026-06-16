from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redis.asyncio as redis
from contextlib import asynccontextmanager

from app.config import config
from app.config.logconfig import LOGGING_CONFIG

from app.routers import image as image_router

from app.routers import food as food_router
from app.routers import meal as meal_router

from app.routers import normcpfc as normcpfc_router
from app.routers import userdata as userdata_router
from app.routers import user as user_router

from app.routers import statisticwh as statisticwh_router
from app.routers import statisticcpfc as statisticcpfc_router
from app.routers import userstatistic as userstatistic_router

from app.utils.logger import Colors, log_request_info, log_response_info

import logging
from logging.config import dictConfig
import time
import uuid
import os

redis_url = os.getenv("REDIS_URL")  # или "KV_URL", проверьте в настройках проекта
if not redis_url:
    # Значение по умолчанию для локальной разработки
    redis_url = "redis://localhost:6379"

tidb_host = os.getenv("TIDB_HOST")
tidb_port = os.getenv("TIDB_PORT", "4000")
tidb_user = os.getenv("TIDB_USER")
tidb_password = os.getenv("TIDB_PASSWORD")
tidb_database = os.getenv("TIDB_DATABASE")

if tidb_host and tidb_user and tidb_password and tidb_database:
    config.settings.DATABASE_URL = f"mysql+aiomysql://{tidb_user}:{tidb_password}@{tidb_host}:{tidb_port}/{tidb_database}"
else:
    # fallback для локальной разработки (или ошибка)
    config.settings.DATABASE_URL = "mysql+aiomysql://fastapi_user:userpassword123@localhost:3306/newschema"

@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_client = redis.from_url(redis_url, encoding="utf-8")
    await FastAPILimiter.init(redis_client)
    yield
    await FastAPILimiter.close()

app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight": True},
    lifespan=lifespan
)

rl_times = config.settings.rate_limiter_params['Times']
rl_seconds = config.settings.rate_limiter_params['Seconds']

# Если мы на Vercel (переменная VERCEL_ENV устанавливается автоматически)
if os.getenv("VERCEL_ENV"):
    # Простая настройка: все логи пишутся в консоль
    logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
else:
    # Ваша локальная конфигурация с файлами
    dictConfig(LOGGING_CONFIG)
    
logger = logging.getLogger("myapp")

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("https")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    
    await log_request_info(request, request_id)
    
    start_time = time.time()
    
    try:
        response = await call_next(request)
    except Exception as exc:
        short_id = request_id[:8]
        print(f"\n{Colors.BOLD}{Colors.RED}╔═══════════════════════════════════════════════════════════════{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.RED}║ 💥 ERROR [{short_id}]{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.RED}╠═══════════════════════════════════════════════════════════════{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.WHITE}║ {Colors.RED}Exception: {str(exc)}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.RED}╚═══════════════════════════════════════════════════════════════{Colors.RESET}\n")
        raise
    
    processing_time = time.time() - start_time
    await log_response_info(response, request_id, processing_time)
    
    return response

app.include_router(image_router.router,
                   prefix=config.settings.api_strings['General'],
                   tags=["Анализ изображения"],
                   dependencies=[Depends(RateLimiter(times=rl_times, seconds=rl_seconds))]
                   )

app.include_router(food_router.router,
                   prefix=config.settings.api_strings['General'],
                   tags=["Продукты"],
                   dependencies=[Depends(RateLimiter(times=rl_times, seconds=rl_seconds))]
                   )


# USER ROUTERS
app.include_router(normcpfc_router.router,
                   prefix=config.settings.api_strings['User']["Data"],
                   tags=["Нормы КБЖУ пользователя"],
                   dependencies=[Depends(RateLimiter(times=rl_times, seconds=rl_seconds))]
                   )
app.include_router(userdata_router.router,
                   prefix=config.settings.api_strings['User']["Data"],
                   tags=["Данные пользователя"],
                   dependencies=[Depends(RateLimiter(times=rl_times, seconds=rl_seconds))]
                   )
app.include_router(user_router.router,
                   prefix=config.settings.api_strings['User']["Data"],
                   tags=["Получение пользователя"],
                   dependencies=[Depends(RateLimiter(times=rl_times, seconds=rl_seconds))]
                   )
app.include_router(meal_router.router,
                   prefix=config.settings.api_strings['User']["Data"],
                   tags=["Приемы пищи пользователя"],
                   dependencies=[Depends(RateLimiter(times=rl_times, seconds=rl_seconds))]
                   )

# STATISTIC ROUTERS
app.include_router(statisticwh_router.router,
                   prefix=config.settings.api_strings['User']["Statistic"],
                   tags=["Статистика по росту/весу"],
                   dependencies=[Depends(RateLimiter(times=rl_times, seconds=rl_seconds))]
                   )
app.include_router(statisticcpfc_router.router,
                   prefix=config.settings.api_strings['User']["Statistic"], 
                   tags=["Статистика по КБЖУ"],
                   dependencies=[Depends(RateLimiter(times=rl_times, seconds=rl_seconds))]
                   )
app.include_router(userstatistic_router.router,
                   prefix=config.settings.api_strings['User']["Statistic"],
                   tags=["Статистика пользователя"],
                   dependencies=[Depends(RateLimiter(times=rl_times, seconds=rl_seconds))]
                   )

@app.get("/")
async def read_root():
    return {"message": "Hello World"}