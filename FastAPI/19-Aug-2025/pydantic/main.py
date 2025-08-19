from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
items = []

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return item
@app.get("/items/")
def get():
    return{"all items": items}
