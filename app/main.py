from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas, crud
from .database import engine, Base, SessionLocal

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(lifespan=lifespan)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.get("/widgets/", response_model=list[schemas.Widget])
async def read_widgets(db: AsyncSession = Depends(get_db)):
    return await crud.get_widgets(db)

@app.post("/widgets/", response_model=schemas.Widget)
async def create_widget(widget: schemas.WidgetCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_widget(db, widget)
