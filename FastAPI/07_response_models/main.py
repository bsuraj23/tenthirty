from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

class ResponseModel(BaseModel):
    items: List[Item]
    count: int

@app.get("/items/", response_model=ResponseModel)
def get_items():
    items = [Item(name="item1", price=10.0), Item(name="item2", price=20.0)]
    return {"items": items, "count": len(items)}
