import ssl
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import config

def create_db_engine():
    ssl_context = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    
    return create_async_engine(
        config.settings.database_url,
        connect_args={"ssl": ssl_context},
        echo=False
    )

engine = create_db_engine()
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session