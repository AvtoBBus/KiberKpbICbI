from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

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

import logging
from logging.config import dictConfig
import time
import uuid
from app.utils.logger import Colors, log_request_info, log_response_info


app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight": True}
)

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("myapp")

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
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
                   tags=["Анализ изображения"]
                   )

app.include_router(food_router.router,
                   prefix=config.settings.api_strings['General'],
                   tags=["Продукты"]
                   )


# USER ROUTERS
app.include_router(normcpfc_router.router,
                   prefix=config.settings.api_strings['User']["Data"],
                   tags=["Нормы КБЖУ пользователя"]
                   )
app.include_router(userdata_router.router,
                   prefix=config.settings.api_strings['User']["Data"],
                   tags=["Данные пользователя"])
app.include_router(user_router.router,
                   prefix=config.settings.api_strings['User']["Data"],
                   tags=["Получение пользователя"],
                   )
app.include_router(meal_router.router,
                   prefix=config.settings.api_strings['User']["Data"],
                   tags=["Приемы пищи пользователя"]
                   )

# STATISTIC ROUTERS
app.include_router(statisticwh_router.router,
                   prefix=config.settings.api_strings['User']["Statistic"],
                   tags=["Статистика по росту/весу"]
                   )
app.include_router(statisticcpfc_router.router,
                   prefix=config.settings.api_strings['User']["Statistic"], 
                   tags=["Статистика по КБЖУ"]
                   )
app.include_router(userstatistic_router.router,
                   prefix=config.settings.api_strings['User']["Statistic"],
                   tags=["Статистика пользователя"]
                   )
