# Creating and using dependencies in FastAPI
# from fastapi import FastAPI, Depends

# def get_query(query: str = None):
#     return query

# app = FastAPI()

# @app.get("/items/")
# def read_items(query: str = Depends(get_query)):
#     return {"query": query}

# Creating and using dependencies in FastAPI
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

# Dependency function
def get_query(query: str = None):
    return query

# Pydantic model for POST
class Item(BaseModel):
    name: str
    price: float

# GET endpoint
@app.get("/items/")
def read_items(query: str = Depends(get_query)):
    return {"query": query}

# POST endpoint
@app.post("/items/")
def create_item(item: Item, query: str = Depends(get_query)):
    return {
        "message": "Item created successfully",
        "item": item,
        "query": query
    }
#PUT endpoint
@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item, query:str = Depends(get_query)):
    return {
        "message": f"Item {item_id} updated successfully",
        "updated_item": item,
        "query": query
    }


