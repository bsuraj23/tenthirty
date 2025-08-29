from fastapi import FastAPI, HTTPException, Depends, Header

app=FastAPI()

def get_token_header(x_token:str=Header(...)):
    if x_token != "secret123":
        raise HTTPException(status_code=401, detail="missing or Invlid token")
    return x_token

def get_db():
    db={"users":{1:{"id":1,"name":"Harish"}}}
    try:
        yield db
    finally:
        pass

@app.get("/me")
def read_me(token:str=Depends(get_token_header), db:dict=Depends(get_db)):
    user=db["users"][1]
    return {"hello":user["name"]}



