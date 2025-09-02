from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Item(BaseModel):
    Name:str
    price:int
    in_stock:bool
@app.post("/items/")  
def create_item(item:Item):
    return{"received_item":item}
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "item_id": item_id,
        "updated_item": item
    }


