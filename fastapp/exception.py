from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    id:int
    name:str
    email:str
    age:int

fake_db={
    1:{"id":1,"name":"Harish","email":"harish@gmail.com","age":21},
    2:{"id":2,"name":"Ashish","email":"ashish@gmail.com","age":22}
}

@app.put("/user/{user_id}")
def update_user(user_id:int, updated_user:User):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="No, their is no user")
    fake_db[user_id]=updated_user.dict()
    return{"Message":"Updated successfully", "user":updated_user}