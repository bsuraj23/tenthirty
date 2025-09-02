from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/{item_id}")
def create_item(item_id: int, name: str):
    items[item_id] = {"name": name}
    return {"message": "Item created", "item": items[item_id]}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    items[item_id] = {"name": name}
    return {"message": "Item updated", "item": items[item_id]}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    deleted_item = items.pop(item_id, {"name": "Not found"})
    return {"message": "Item deleted", "item": deleted_item}

