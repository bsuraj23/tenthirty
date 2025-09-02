from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


items = {}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    items[item_id] = item
    return items[item_id]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    items[item_id] = item
    return items[item_id]
