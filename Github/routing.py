from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Route for homepage
def home():
    return {"message": "Welcome to the homepage"}

@app.get("/about")  # Route for /about
def about():
    return {"message": "This is the about page"}
