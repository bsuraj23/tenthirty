from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

@app.get("/products/{product_id}")
def read_product(product_id: str):
    return {"product_id": product_id}

@app.get("/users")
def read_all_users():
    users = [
        {"user_id": 1, "name": "Navadeep"},
        {"user_id": 2, "name": "Chandu"},
        {"user_id": 3, "name": "Nithish"}
    ]
    return {"users": users}

@app.get("/docs")
def get_docs():
    return {"docs_url":"http://127.0.0.1:8000/docs"}





