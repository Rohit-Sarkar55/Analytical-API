# from pydantic import BaseModel, Field

from typing import List, Optional
from datetime import timezone, datetime
import sqlmodel
from sqlmodel import SQLModel, Field
from timescaledb import TimescaleModel
from timescaledb.utils import get_utc_now

# def get_utc_now():
#     return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)


#Optional for Optional Value
#Field for Default Value
class EventModel (TimescaleModel,table=True):
    # id: Optional[int] = Field(default=None, primary_key=True)
    # id:int
    # page: Optional[str] = ""
    page:str= Field(index=True)
    description: Optional[str] = ""
    # created_at: datetime = Field(
    #     default_factory= get_utc_now,
    #     sa_type = sqlmodel.DateTime(timezone=True),
    #     nullable=False
    # )
    updated_at: datetime = Field(
        default_factory= get_utc_now,
        sa_type = sqlmodel.DateTime(timezone=True),
        nullable=False
    )

    __chunk_time_interval__ = "INTERVAL 1 day"
    __drop_after__ = "INTERVAL 3 days"

class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int

class EventCreateSchema(SQLModel):
    page: str

class EventUpdateSchema(SQLModel):
    description: str