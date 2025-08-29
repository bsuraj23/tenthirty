from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database simulation
fake_db = {
    1: {"name": "Laptop", "price": 75000, "is_offer": True},
    2: {"name": "Phone", "price": 30000, "is_offer": False},
}

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return item

# ✅ PUT endpoint with exception handling
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # Check if item exists
    if item_id not in fake_db:
        raise HTTPException(
            status_code=404,
            detail=f"Item with ID {item_id} not found"
        )
    
    # Extra validation (example: price must be positive)
    if item.price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Price must be greater than zero"
        )
    
    # Update item
    fake_db[item_id] = item.dict()
    return {"message": "Item updated successfully", "item": fake_db[item_id]}
