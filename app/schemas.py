from pydantic import BaseModel

class WidgetBase(BaseModel):
    name: str
    description: str

class WidgetCreate(WidgetBase):
    pass

class Widget(WidgetBase):
    id: int

    class Config:
        orm_mode = True
