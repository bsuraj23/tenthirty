from fastapi import FastAPI
from enum import Enum
app = FastAPI()


class Category(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    food = "food"

@app.get("/category/{category_name}")
def get_category(category_name: Category):
    return {"category": category_name}
