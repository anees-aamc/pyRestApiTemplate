# app/db.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
from logging import getLogger

load_dotenv()

logger = getLogger('uvicorn.error')

DATABASE_URL = (
    f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=False, future=True)

# Async session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession,
)

# Declarative base for ORM models
Base = declarative_base()


# @asynccontextmanager
async def get_db():
    """Async DB dependency for FastAPI."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            logger.info("get_db: exception:", e)
            raise
        finally:
            await session.close()
