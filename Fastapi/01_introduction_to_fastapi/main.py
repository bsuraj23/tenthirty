from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI! Server is respoding successfully."}
@app.get("/docs")
def get_docs():
    return {"docs_url": "http://127.0.0.1:8000/docs"}
