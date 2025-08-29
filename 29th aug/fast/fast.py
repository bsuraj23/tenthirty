from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Product model
class Product(BaseModel):
    id: int
    name: str
    price: float

# Buyer model
class Buyer(BaseModel):
    buyer_name: str
    product_id: int

# In-memory storage
products: List[Product] = []
purchases: List[dict] = []


@app.post("/add_product/")
def add_product(product: Product):
    # Check if product already exists
    for p in products:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="Product already exists")
    products.append(product)
    return {"message": "Product added successfully", "product": product}


@app.get("/products/")
def get_products():
    return products


@app.post("/buy_product/")
def buy_product(buyer: Buyer):
    # Check if product exists
    product = next((p for p in products if p.id == buyer.product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Save purchase
    purchase = {"buyer_name": buyer.buyer_name, "product": product}
    purchases.append(purchase)
    return {"message": f"{buyer.buyer_name} bought {product.name}", "purchase": purchase}


@app.get("/purchases/")
def get_purchases():
    return purchases
