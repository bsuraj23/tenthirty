from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

items_db = {}

@app.get("/items/")
def get_items():
    return items_db

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items_db.get(item_id, {"error": "Item not found"})

@app.post("/items/")
def create_item(item: Item):
    new_id = len(items_db) + 1
    items_db[new_id] = item.dict()
    return {"id": new_id, **item.dict()}


