from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Address(BaseModel):
    street: str
    city: str
    zipcode: str

class Student(BaseModel):
    name: str
    age: int
    address: Address   # Nested object

@app.post("/students/")
def add_student(student: Student):
    return {"message": "Student added", "data": student}
