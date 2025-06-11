# from pydantic import BaseModel, Field

from typing import List, Optional
from datetime import timezone, datetime
import sqlmodel
from sqlmodel import SQLModel, Field

def get_utc_now():
    return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)


#Optional for Optional Value
#Field for Default Value
class EventModel (SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # id:int
    page: Optional[str] = ""
    description: Optional[str] = ""
    created_at: datetime = Field(
        default_factory= get_utc_now,
        sa_type = sqlmodel.DateTime(timezone=True),
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory= get_utc_now,
        sa_type = sqlmodel.DateTime(timezone=True),
        nullable=False
    )

class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int

class EventCreateSchema(SQLModel):
    page: str

class EventUpdateSchema(SQLModel):
    description: str