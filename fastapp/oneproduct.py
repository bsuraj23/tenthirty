from fastapi import FastAPI, HTTPException

app=FastAPI()

db={
    "laptop":{"name":"Laptop","price":80000,"brand":"hp"},
    "phone":{"name":"Mobile","price":20000,"brand":"xiaomi"},
    "tab":{"name":"tab","price":50000,"brand":"apple"}
}

@app.get("/products")
def get_all_products():
    return {"Products":list(db.values())}

@app.get("/product/{name}")
def single_product(name:str):
    product=db.get(name.lower())
    if not product:
        raise HTTPException(status_code=404, detail="No product found")
    return product