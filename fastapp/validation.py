from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

user_details={}
count_id=1

class User(BaseModel):
    name:str
    age:int 
    phone:int
    email:str

@app.post("/create")
def create_user(user:User):
    global count_id
    user_details[count_id]=user
    count_id += 1
    return user

@app.get("/users")
def get_users():
    return user_details
