from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    code: str = Field(..., pattern=r"^[A-Z]{3}-\d{3}$")

app = FastAPI()

# temporary in-memory "database"
products_db: List[Product] = []

# POST API - add a product
@app.post("/products/")
def create_product(product: Product):
    products_db.append(product)
    return {"message": "Product added successfully", "product": product}

# GET API - get all products
@app.get("/products/")
def get_all_products():
    return {"total_products": len(products_db), "products": products_db}
