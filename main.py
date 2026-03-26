from fastapi import FastAPI, UploadFile, File, Request
import shutil
from pydantic import BaseModel
from pathlib import Path
from fastapi.responses import FileResponse, HTMLResponse 
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"),name="static")
templates = Jinja2Templates(directory='frontend')
@app.get("/", response_class= HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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