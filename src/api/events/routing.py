from fastapi import APIRouter
from .schemas import EventSchema , EventListSchema , EventCreateSchema, EventUpdateSchema
router = APIRouter()


@router.get("/")
def read_events() -> EventListSchema:
    results = [{"id":1},{"id":2},{"id":4}]
    return {
        "results": results,
        "count": len(results)
    }

@router.post("/")  #same url one acting as get another one as post method
def create_events(payload: EventCreateSchema) -> EventSchema:
    print(payload)
    return {"id":123}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id": event_id}

@router.put("/{event_id}")
def update_event(event_id:int, payload: EventUpdateSchema) -> EventSchema:
    print(payload)
    return {"id":event_id}