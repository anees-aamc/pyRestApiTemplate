import asyncio
from app.db import engine, Base
from app import models  # make sure models are imported before running

async def init_models(drop_existing: bool=False):
    async with engine.begin() as conn:
        if drop_existing:
            # Drop all tables (optional)
            await conn.run_sync(Base.metadata.drop_all)
        # Create all tables
        print('Creating tables')
        await conn.run_sync(Base.metadata.create_all)
        print('Done')

if __name__ == "__main__":
    asyncio.run(init_models())
