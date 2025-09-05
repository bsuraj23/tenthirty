from fastapi import FastAPI
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    code: str = Field(..., pattern=r"^[A-Z]{3}-\d{3}$")

app = FastAPI()

# Temporary in-memory storage
products_db = []

@app.post("/products/")
def create_product(product: Product):
    products_db.append(product)
    return {"message": "Product created successfully", "product": product}

@app.get("/products/")
def get_products():
    return {"count": len(products_db), "products": products_db}