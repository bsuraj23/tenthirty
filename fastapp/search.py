from fastapi import FastAPI
from typing import Optional

app = FastAPI()

products=[
    {"id":1,"name":"Pen","category":"Stationery","price":30},
    {"id":2,"name":"Notebook","category":"Stationery","price":120},
    {"id":3,"name":"T-shirt","category":"Clothing","price":250},
    {"id":4,"name":"Eraser","category":"Stationery","price":10},
    {"id":5,"name":"Mouse","category":"Electronics","price":500},   
]

@app.get("/products")
def search_products(category:Optional[str]=None,max_price:Optional[int]=None):
    filter_products=products
    if category:
        filter_products=[p for p in filter_products if p["category"].lower()==category.lower()]
    if max_price:
        filter_products=[p for p in filter_products if p["price"]<=max_price]
    return filter_products
