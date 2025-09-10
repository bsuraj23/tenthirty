from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Pydantic model
class User(BaseModel):
    name: str
    age: int

app = FastAPI()

# temporary in-memory database
users_db: List[User] = []

# POST API - create user
@app.post("/users/")
def create_user(user: User):
    users_db.append(user)  # store user in list
    return {"message": "User added", "user": user}

# GET API - get all users
@app.get("/users/")
def get_all_users():
    return {"total_users": len(users_db), "users": users_db}
