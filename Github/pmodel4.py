from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True


products_db = {}


@app.post("/products/")
def add_product(product: Product):
    products_db[product.name] = product
    return {"message": "Product added", "data": product}


@app.get("/products/{name}")
def get_product(name: str):
    return {"data": products_db.get(name, "Product not found")}


@app.put("/products/{name}")
def update_product(name: str, updated: Product):
    products_db[name] = updated
    return {"message": "Product updated", "data": updated}

@app.delete("/products/{name}")
def delete_product(name: str):
    deleted = products_db.pop(name, "Product not found")
    return {"message": "Product deleted", "data": deleted}
