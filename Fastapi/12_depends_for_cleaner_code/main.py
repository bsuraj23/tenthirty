# Using Depends() for cleaner code
from fastapi import FastAPI, Depends

def get_token():
    return "mysecrettoken"

app = FastAPI()

@app.get("/secure/")
def secure_route(token: str = Depends(get_token)):
    return {"token": token}
