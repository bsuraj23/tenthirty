from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

# temporary storage
users_db = []  # list of User objects

@app.post("/users/")
def create_user(user: User):
    users_db.append(user)  # store user in memory
    return {"message": "User created successfully", "user": user}

@app.get("/users/")
def get_users():
    return {"count": len(users_db), "users": users_db}