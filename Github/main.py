from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message":"Hello, welcome to Fastapi!"}

@app.post("/create/")
def create_item(item: str):
    return {"message": "Item created successfully!", "item": item}

@app.put("/update/{item_id}")
def update_item(item_id: int, item: str):
    return {"message": f"Item {item_id} updated successfully!", "updated_item": item}    