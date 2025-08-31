from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    id:int
    name:str
    age:int
    password:str

class UserPublic(BaseModel):
    id:int
    name:str
    age:int

users_db=[
    User(id=1,name="Harish",age=21,password="secret123"),
    User(id=2,name="Ashish",age=22,password="strig"),
]

@app.get("/users", response_model=list[UserPublic])
def get_users():
    return users_db

@app.get("/user/{user_id}", response_model=UserPublic)
def get_user(user_id:int):
    for user in users_db:
        if user.id == user_id:
            return user
    return{"error":"No user found"}

