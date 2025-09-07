from fastapi import FastAPI, Depends

def get_query(query: str = None):
    return query

app = FastAPI()

@app.get("/items/")
def read_items(query: str = Depends(get_query)):
    return {"query": query}