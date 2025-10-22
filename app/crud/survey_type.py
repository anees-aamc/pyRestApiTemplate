from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import SurveyType as SurveyTypeModel
from app.schema import SurveyType
from app.crud.base import CRUDBase


class CRUDSurveyType(CRUDBase[SurveyTypeModel, SurveyType]):
    async def get_detail(self, db: AsyncSession, survey_type_cd: str) -> SurveyTypeModel | None:
        """Fetch survey with related program and survey type."""
        result = await db.execute(
            select(SurveyTypeModel)
            .filter(SurveyTypeModel.survey_type_cd == survey_type_cd)
            .options(
                selectinload(SurveyTypeModel.surveys),
            )
        )
        return result.scalars().first()


survey_type = CRUDSurveyType(SurveyTypeModel)
