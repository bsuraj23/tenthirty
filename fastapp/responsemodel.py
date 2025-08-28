from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app=FastAPI()

class User(BaseModel):
    id:int
    username:str
    email:str
    is_admin:bool
    password:str

class UserPublic(BaseModel):
    id:int
    username:str
    email:str

fake_db={
    1:{"id":1,"username":"Harish","email":"harish@gmail.com","is_admin":True,"password":"game123"},
    2:{"id":2,"username":"Manish","email":"manish@gmail.com","is_admin":False,"password":"game143"}

}

@app.get("/users/{user_id}",response_model=UserPublic)
def get_user(user_id:int):
    user=fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404,detail="No User found")
    return user

@app.get("/users",response_model=list[UserPublic])
def list_users():
    return list(fake_db.values())
