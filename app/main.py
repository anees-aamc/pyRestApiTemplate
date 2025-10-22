from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from logging import getLogger
from app.db import get_db
from app.crud import program, survey, survey_type
from app.schema import Program, ProgramDetail, Survey, SurveyDetail, SurveyType

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


@app.get("/surveys", response_model=list[Survey])
async def list_surveys(db: AsyncSession = Depends(get_db)):
        db_objs = await survey.get_all(db)
        logger.info(f"list_surveys: listing {len(db_objs)} surveys")
        res = [Survey.model_validate(o) for o in db_objs]
        return res


@app.get("/surveys/{id}", response_model=SurveyDetail)
async def get_survey(id: int, db: AsyncSession = Depends(get_db)):
    db_obj = await survey.get_detail(db, id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Survey not found")
    return SurveyDetail.model_validate(db_obj)


@app.post("/surveys", response_model=Survey)
async def create_survey(obj_in: Survey, db: AsyncSession = Depends(get_db)):
    db_obj = await survey.create(db, obj_in)
    return Survey.model_validate(db_obj)


@app.get("/survey_types", response_model=list[SurveyType])
async def list_survey_types(db: AsyncSession = Depends(get_db)):
        db_objs = await survey_type.get_all(db)
        logger.info(f"list_survey_types: listing {len(db_objs)} survey_types")
        res = [SurveyType.model_validate(o) for o in db_objs]
        return res


@app.get("/survey_types/{survey_type_cd}", response_model=SurveyType)
async def get_survey_type(survey_type_cd: str, db: AsyncSession = Depends(get_db)):
    db_obj = await survey_type.get_detail(db, survey_type_cd)
    if not db_obj:
        raise HTTPException(status_code=404, detail=f"Survey type `{survey_type_cd}`not found")
    return SurveyType.model_validate(db_obj)


@app.post("/survey_types", response_model=SurveyType)
async def create_survey_type(obj_in: SurveyType, db: AsyncSession = Depends(get_db)):
    db_obj = await survey_type.create(db, obj_in)
    return SurveyType.model_validate(db_obj)
