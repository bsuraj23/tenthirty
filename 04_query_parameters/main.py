from fastapi import FastAPI

app = FastAPI()

@app.get("/search/")
def search_items(q: str = None, limit: int = 10):
    return {"query": q, "limit": limit}
@app.get("/docs")
def get_docs():
    return {"docs_url": "http://127.0.0.1:8000/docs"}