from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = {1: {"name": "Laptop", "price": 50000, "is_offer": True}}

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(404, "Item not found")
    items[item_id] = item.dict()
    return {"msg": "Updated", "item": items[item_id]}
