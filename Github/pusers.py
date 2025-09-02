from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Address model
class Address(BaseModel):
    street: str
    city: str
    zipcode: str

# Customer model
class Customer(BaseModel):
    name: str
    email: str
    address: Address  # nested model

# User model (for authentication / login purposes)
class User(BaseModel):
    username: str
    password: str


# Endpoint for adding customers
@app.post("/customers/")
def add_customer(customer: Customer):
    return {"message": "Customer added", "data": customer}


# Endpoint for creating a user
@app.post("/users/")
def create_user(user: User):
    return {"message": "User created", "data": user}


# Endpoint for login
@app.post("/login/")
def login(user: User):
    if user.username == "admin" and user.password == "1234":
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}
