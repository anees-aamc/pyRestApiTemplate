import asyncio
from sqlalchemy import text
from app.db import engine

async def test_conn():
    async with engine.begin() as conn:
        query = "SELECT 1"
        result = await conn.execute(text(query))
        print(result.all())

asyncio.run(test_conn())