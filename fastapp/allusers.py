from fastapi import FastAPI

app=FastAPI()

user_db={
    1:{"id":1,"name":"Harish","age":21},
    2:{"id":2,"name":"Ashish","age":22}
}

@app.get("/users")
def get_all_users():
    return {"users":list(user_db.values())}