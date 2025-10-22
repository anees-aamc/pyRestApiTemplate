from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Survey as SurveyModel
from app.schema import Survey, SurveyDetail
from app.crud.base import CRUDBase


class CRUDSurvey(CRUDBase[SurveyModel, Survey]):
    async def get_detail(self, db: AsyncSession, id: int) -> SurveyModel | None:
        """Fetch survey with related program and survey type."""
        result = await db.execute(
            select(SurveyModel)
            .filter(SurveyModel.id == id)
            .options(
                selectinload(SurveyModel.program),
                selectinload(SurveyModel.survey_type_cd),
                # selectinload(SurveyModel.survey_data),
                # selectinload(SurveyModel.crosswalks),
            )
        )
        return result.scalars().first()


survey = CRUDSurvey(SurveyModel)
