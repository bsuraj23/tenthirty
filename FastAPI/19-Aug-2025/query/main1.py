
from fastapi import FastAPI

app = FastAPI()

items = ["Mani","rambo","dikar"]


@app.get("/search/")
def search(q: str = None, limit: int = 10):
    if q:
        result = [item for item in items if q.lower() in item.lower()]
    else:
        result = items 
    return{"query":q,"results": result[:limit]}

@app.get("/docs")
def get_docs():
    return {"docs_url": "http://127.0.0.1:8000/docs"}