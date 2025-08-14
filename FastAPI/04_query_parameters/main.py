from fastapi import FastAPI

app = FastAPI()

@app.get("/search/")
def search_items(q: str = None, limit: int = 10):
    return {"query": q, "limit": limit}
