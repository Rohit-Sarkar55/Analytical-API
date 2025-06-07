from pydantic import BaseModel, Field
from typing import List, Optional

#Optional for Optional Value
#Field for Default Value
class EventSchema (BaseModel):
    id: int
    page: Optional[str] = ""
    description: Optional[str] = Field(default='My Description')

class EventListSchema(BaseModel):
    results: List[EventSchema]
    count: int

class EventCreateSchema(BaseModel):
    page: str

class EventUpdateSchema(BaseModel):
    description: str