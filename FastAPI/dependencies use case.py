from fastapi import FastAPI, Depends

def get_db():
    # Simulate a database session
    db = {"users": ["Sindhu", "Chinnu"]}
    return db

def get_current_user():
    # Simulate authentication
    return "Sindhu"

def log_request():
    # Simulate logging
    print("Request logged!")

app = FastAPI()

@app.get("/users/")
def read_users(db=Depends(get_db), user=Depends(get_current_user), log=Depends(log_request)):
    return {"current_user": user, "users": db["users"]}