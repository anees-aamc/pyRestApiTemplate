from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def get_widgets(db: AsyncSession):
    result = await db.execute(select(models.Widget))
    return result.scalars().all()

async def create_widget(db: AsyncSession, widget: schemas.WidgetCreate):
    db_widget = models.Widget(**widget.dict())
    db.add(db_widget)
    await db.commit()
    await db.refresh(db_widget)
    return db_widget
