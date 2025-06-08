import os
from fastapi import APIRouter , Depends
from api.db.config import DATABASE_URL
from api.db.session import get_session
from sqlmodel import Session
from .models import EventModel , EventListSchema , EventCreateSchema, EventUpdateSchema

router = APIRouter()



@router.get("/")
def read_events() -> EventListSchema:
    print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    results = [{"id":1},{"id":2},{"id":4}]
    return {
        "results": results,
        "count": len(results)
    }

@router.post("/", response_model=EventModel)  #same url one acting as get another one as post method
def create_events(
    payload: EventCreateSchema, 
    session: Session = Depends(get_session)):

    print(payload.page)
    data= payload.model_dump() # making a dict outof the payload
    obj =  EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    # return {"id":123, **data} #destructuring the data
    return obj


@router.get("/{event_id}")
def get_event(event_id: int) -> EventModel:
    return {"id": event_id}

@router.put("/{event_id}")
def update_event(event_id:int, payload: EventUpdateSchema) -> EventModel:
    print(payload.description)
    return {"id":event_id,"description": payload.description}