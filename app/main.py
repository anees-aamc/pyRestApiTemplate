from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from logging import getLogger
from app.db import get_db
from app.crud import program, survey
from app.schema import Program, ProgramDetail, Survey, SurveyDetail

app = FastAPI()

logger = getLogger('uvicorn.error')

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200",
    "http://127.0.0.1:4200",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    logger.info("root status: ok")
    return {"status": "ok"}


@app.get("/programs", response_model=list[Program])
async def list_programs(db: AsyncSession = Depends(get_db)):
        db_objs = await program.get_all(db)
        logger.info(f"list_programs: listing {len(db_objs)} programs")
        res = [Program.model_validate(o) for o in db_objs]
        return res


@app.get("/programs/{id}", response_model=ProgramDetail)
async def get_program(id: int, db: AsyncSession = Depends(get_db)):
    db_obj = await program.get_detail(db, id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Program not found")
    return ProgramDetail.model_validate(db_obj)


@app.post("/programs", response_model=Program)
async def create_program(obj_in: Program, db: AsyncSession = Depends(get_db)):
    db_obj = await program.create(db, obj_in)
    return Program.model_validate(db_obj)


@app.get("/surveys/{id}", response_model=SurveyDetail)
async def get_survey(id: int, db: AsyncSession = Depends(get_db)):
    db_obj = await survey.get_detail(db, id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Survey not found")
    return SurveyDetail.model_validate(db_obj)
