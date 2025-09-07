from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
from sqlmodel import SQLModel, create_engine, Session, select
from contextlib import asynccontextmanager
from typing import Annotated
from models import User, CreateUser

database_url="sqlite:///./users.db"
engine=create_engine(database_url,echo=True)

@asynccontextmanager
async def lifespan(app:FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app=FastAPI(lifespan=lifespan)

def get_session():
    with Session(engine) as session:
        yield session

session_dep=Annotated[Session, Depends(get_session)]

@app.post("/createuser")
def create_user(user:CreateUser,session:session_dep):
    new_user=User.model_validate(user)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@app.get("/users", response_model=list[User])
def get_users(session:session_dep):
    users=session.exec(select(User)).all()
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users

@app.get("/user/{user_id}", response_model=User)
def get_single_user(user_id:int, session:session_dep):
    user=session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@app.put("/user/{user_id}", response_model=User)
def update_user(user_id:int, update:CreateUser,session:session_dep):
    user=session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    user.name=update.name
    user.phone=update.phone
    user.email=update.email
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.delete("/user/{user_id}")
def delete_user(user_id:int, session:session_dep):
    user=session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    session.delete(user)
    session.commit()
    return {"message":"user deleted successfully"}
