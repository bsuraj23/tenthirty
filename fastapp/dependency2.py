from fastapi import FastAPI, HTTPException, Depends

app=FastAPI()

def get_token():
    return "secret123"

@app.get("/protected")
def protected_route(token:str=Depends(get_token)):
    return {"Token":token}