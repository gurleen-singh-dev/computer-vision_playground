from fastapi import FastAPI, UploadFile, File, Request, Form, HTTPException
import shutil
from pathlib import Path
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
from backend.edge import edges
from backend.gaussian import gaussian
from backend.grayscale import gray

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")
templates = Jinja2Templates(directory='frontend')

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "output_image": None
    })


@app.post("/upload", response_class=HTMLResponse)
async def upload_image(request: Request,
                       file: UploadFile = File(...),
                       operation: str = Form(...)):
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"


    if file is None or file.filename == "":
        raise HTTPException(status_code=400, detail="No file selected")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if operation == "grayscale":
        output_path = gray(file_path)
    elif operation == "edge":
        output_path = edges(file_path)
    elif operation == "gaussian":
        output_path = gaussian(file_path)
    else:
        output_path = file_path

    return templates.TemplateResponse("index.html", {
        "request": request,
        "output_image": output_path
    })
