from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Define User model
class User(BaseModel):
    name: str
    age: int

app = FastAPI()

# In-memory storage for users
users_db: List[User] = []

# POST endpoint to create user
@app.post("/users/")
def create_user(user: User):
    users_db.append(user)
    return {"message": "User created successfully", "user": user}

# GET endpoint to fetch all users
@app.get("/users/")
def get_users():
    return {"users": users_db}
