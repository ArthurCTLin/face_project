import os 
import shutil
from typing import List
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from face_search import crop_faces_and_save, match_target_face

app = FastAPI()

TEMP_DIR = "./temp_uploads"
os.makedirs(TEMP_DIR, exist_ok=True)

@app.post("/crop/")
async def crop_faces(file: UploadFile = File(...)):
    temp_path = os.path.join(TEMP_DIR, file.filename)
    with open(temp_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)

    result_paths = crop_faces_and_save(temp_path)
    return JSONResponse(content={"cropped_paths": result_paths})

@app.post("/crop_batch/")
async def crop_faces_batch(files: List[UploadFile] = File(...)):
    all_cropped_paths = []

    for file in files:
        temp_path = os.path.join(TEMP_DIR, file.filename)
        with open(temp_path, 'wb') as f:
            shutil.copyfileobj(file.file, f)

        cropped_paths = crop_faces_and_save(temp_path)
        all_cropped_paths.append({
            "original_file": file.filename,
            "cropped_faces": cropped_paths
        })
    
    return JSONResponse(content={"all_cropped_paths": all_cropped_paths})
#    return {"results": all_cropped_paths}

@app.post("/match/")
async def match_face(
        file: UploadFile = File(...),
        storage_path: str = Form("./"),
        ):
    temp_path = os.path.join(TEMP_DIR, file.filename)
    with open(temp_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    matches = match_target_face(temp_path, storage_folder=storage_path)
    return JSONResponse(content={"matches": matches})
