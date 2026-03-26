from fastapi import FastAPI, UploadFile, File, Request, Form
import shutil
from pydantic import BaseModel
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

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.get("/", response_class=HTMLResponse)
# def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/upload", response_class=HTMLResponse)
# async def upload_image(request: Request,
#                        file: UploadFile = File(...),
#                        operation: str = Form(...)):
#     file_path = f"{UPLOAD_FOLDER}/{file.filename}"

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     if operation == "grayscale":
#         output_path = convert_to_grayscale(file_path)
#     elif operation == "edge":
#         output_path = detect_edges(file_path)
#     else:
#         output_path = file_path

#     return templates.TemplateResponse("index.html", {
#         "request": request,
#         "output_image": output_path
#     })

# @app.post("/upload-image")
# def upload_image(file: UploadFile = File(...)):

#     file_location = f"backend/uploads/{file.filename}"

#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {
#         "message": "Image uploaded successfully",
#         "filename": file.filename
#     }
# @app.get("/get_image")
# def get_image():
#     image_path = Path("backend/uploads/arch.png")
#     if not image_path.is_file():
#         return("error: no file found")
#     return FileResponse(image_path)
