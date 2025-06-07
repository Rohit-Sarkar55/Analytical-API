# from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field
from typing import List, Optional

#Optional for Optional Value
#Field for Default Value
class EventModel (SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # id:int
    page: Optional[str] = ""
    description: Optional[str] = ""

class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int

class EventCreateSchema(SQLModel):
    page: str

class EventUpdateSchema(SQLModel):
    description: str