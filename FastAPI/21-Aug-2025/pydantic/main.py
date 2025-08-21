from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# here base model is parent class via OOPS concept
class item(BaseModel):
    name: str
    price: float
    description: str = None
    

@app.post("/items/")
def create(item: item):
    return item