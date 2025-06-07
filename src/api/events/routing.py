import os
from fastapi import APIRouter
from .models import EventModel , EventListSchema , EventCreateSchema, EventUpdateSchema
router = APIRouter()
from api.db.config import DATABASE_URL


@router.get("/")
def read_events() -> EventListSchema:
    print(os.environ.get("DATABASE_URL"),DATABASE_URL)
    results = [{"id":1},{"id":2},{"id":4}]
    return {
        "results": results,
        "count": len(results)
    }

@router.post("/")  #same url one acting as get another one as post method
def create_events(payload: EventCreateSchema) -> EventModel:
    print(payload.page)
    data= payload.model_dump() # making a dict outof the payload
    return {"id":123, **data} #destructuring the data


@router.get("/{event_id}")
def get_event(event_id: int) -> EventModel:
    return {"id": event_id}

@router.put("/{event_id}")
def update_event(event_id:int, payload: EventUpdateSchema) -> EventModel:
    print(payload.description)
    return {"id":event_id,"description": payload.description}