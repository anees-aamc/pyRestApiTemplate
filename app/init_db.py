import asyncio
from app.db import engine
from app.models import Base
from app import models


async def init_db(drop_existing: bool=False):
    """Create all database tables."""
    async with engine.begin() as conn:
        if drop_existing:
            print("Dropping existing tables (if any)...")
            await conn.run_sync(Base.metadata.drop_all)
        print("Creating tables...")
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database initialization complete.")


if __name__ == "__main__":
    asyncio.run(init_db())
