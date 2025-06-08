import os
from fastapi import APIRouter , Depends , HTTPException
from api.db.config import DATABASE_URL
from api.db.session import get_session
from sqlmodel import Session , select
from .models import EventModel , EventListSchema , EventCreateSchema, EventUpdateSchema

router = APIRouter()



@router.get("/",response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)) :
    # print(os.environ.get("DATABASE_URL"), DATABASE_URL)

    query = select(EventModel).order_by(EventModel.id.desc()).limit(5)
    results = session.exec(query).all()

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


@router.get("/{event_id}",response_model=EventModel)
def get_event(event_id: int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404, detail="event not found")
    return result


@router.put("/{event_id}")
def update_event(event_id:int, payload: EventUpdateSchema) -> EventModel:
    print(payload.description)
    return {"id":event_id,"description": payload.description}