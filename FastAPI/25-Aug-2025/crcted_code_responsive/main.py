from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str

class Student(BaseModel):
    name: str
    id: int

class ResponseModel(BaseModel):
    #here the items is replaced to students  run the code 
    students: List[Item]
    count: int

@app.get("/coolie", response_model=ResponseModel)
def get_functionName():
    items = [Item(name="Vinay")] 
    return {"students": items, "count": len(items)}


# @app.get("/items/", response_model=ResponseModel)
# def get_items():
#     items = [Item(name="item1", price=10.0),
#     Item(name="item2", price=20.0), Item (name="item3", price=34.0) ,]
#     return {"items": items, "count": len (items)}