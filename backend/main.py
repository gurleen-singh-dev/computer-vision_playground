from fastapi import FastAPI, UploadFile, File
import shutil
from pathlib import Path
from fastapi.responses import FileResponse 
app = FastAPI()

@app.post("/upload-image")
def upload_image(file: UploadFile = File(...)):

    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Image uploaded successfully",
        "filename": file.filename
    }
@app.get("/get_image")
def get_image():
    image_path = Path("uploads/arch.png")
    if not image_path.is_file():
        return("error: no file found")
    return FileResponse(image_path)