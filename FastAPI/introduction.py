from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World, Welcome to FastAPI"}

@app.get("/docs")
def read_docs():
    return {"docs_url": "http://127.0.0.1:8000/docs"}
