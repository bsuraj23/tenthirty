from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
app=FastAPI()

@app.post("/upload")
def upload_file(name:str=Form(...), file:UploadFile=File(...)):
    return JSONResponse(content= {"filename":file.filename,"name":name})
