from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

app=FastAPI()

class Address(BaseModel):    #nested model: Address  --> nested model: a model inside another model
    city:str
    pincode:str

    @validator("pincode")   #custom validation: pincode must be 6 digit
    def validation_pincode(cls,v):
        if len(v) != 6 or not v.isdigit():
            raise HTTPException(status_code=404, detail="Pincode must be 6 digits")
        return v

class User(BaseModel):  #main model:User
    name:str
    age:int
    address:Address   #nested model inside User

    @validator("age")  #custom validation: age must be atleast 18,  custom validation means our own rules for checking data
    def check_age(cls,v):
        if v < 18:
            raise HTTPException(status_code=404, detail="Age must be atleast 18")
        return v
    
@app.post("/user")
def create_user(user:User):
    return {"message":"User created successfully", "user":user}




