from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

@app.get("/products/{product_id}")
def read_product(product_id: str):
    return {"product_id": product_id}
    