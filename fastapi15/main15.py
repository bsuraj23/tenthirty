from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    code: str = Field(..., pattern=r"^[A-Z]{3}-\d{3}$")  # Example: ABC-123

app = FastAPI()

# In-memory storage
products_db: List[Product] = []

# POST - Create product
@app.post("/products/")
def create_product(product: Product):
    products_db.append(product)
    return {"message": "Product created successfully", "product": product}

# GET - Fetch all products
@app.get("/products/")
def get_all_products():
    return {"products": products_db}

# GET - Fetch only product names
@app.get("/products/items/")
def get_all_items():
    return {"items": [product.name for product in products_db]}

# GET - Fetch product by name
@app.get("/products/{name}")
def get_product_by_name(name: str):
    for product in products_db:
        if product.name.lower() == name.lower():
            return product
    raise HTTPException(status_code=404, detail=f"Product with name '{name}' not found")
