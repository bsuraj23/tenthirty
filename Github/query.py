from fastapi import FastAPI

app = FastAPI()

items = {}
@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    
    return {"items": list(items.values())[skip: skip + limit]}

@app.post("/items/{item_id}")
def add_item(item_id: int, name: str):
    items[item_id] = {"id": item_id, "name": name}
    return {"message": "Item added", "item": items[item_id]}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    items[item_id] = {"id": item_id, "name": name}
    return {"message": "Item updated", "item": items[item_id]}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    deleted = items.pop(item_id, {"id": item_id, "name": "Not found"})
    return {"message": "Item deleted", "item": deleted}
