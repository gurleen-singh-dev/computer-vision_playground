from fastapi import FastAPI, UploadFile, File
import shutil

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
