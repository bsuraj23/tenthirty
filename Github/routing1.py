from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return ["item1", "item2"]

@app.post("/items")
def create_item(item: dict):
    return {"created": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}