from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI() 


class Order(BaseModel):
    customer_name: str
    items: List[str]

@app.post("/orders/")
def create_order(order: Order):
    return {"message": "Order placed", "order_details": order}
