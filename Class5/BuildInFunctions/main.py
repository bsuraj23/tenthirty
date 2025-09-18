from fastapi import FastAPI

app = FastAPI()

def index ():

    return {"message": "Hello World"}
