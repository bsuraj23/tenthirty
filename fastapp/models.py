from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id:Optional[int]=Field(default=None, primary_key=True)
    name:str
    phone:int
    email:str
class CreateUser(SQLModel):
    name:str
    phone:int
    email:str