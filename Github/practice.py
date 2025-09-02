from fastapi import FastAPI
app=FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id:int):
    return{"user_id": user_id}
@app.get("/products/{products_id}") 
def read_user(product_id:int):
    return{"product_id":product_id}   



