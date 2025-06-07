from typing import Union

from fastapi import FastAPI
from api.events import router as event_router


app = FastAPI()
app.include_router(event_router, prefix="/api/events")


@app.get("/")
def read_root():
    return {"Hello": "Worlders"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/list/{param}")
def read_item(param: int, q: Union[str, None] = None):
    return {"item_id": param, "q": "Rohit"}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}