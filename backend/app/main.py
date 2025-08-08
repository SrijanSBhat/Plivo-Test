from fastapi import FastAPI, File, UploadFile, HTTPException, Header
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
import shutil
import os

from app.pipelines.audio_pipeline import process_audio
from app.pipelines.image_pipeline import process_image
from app.pipelines.doc_pipeline import process_document

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(title="Playground Backend")

# Dummy credentials
DUMMY_USERNAME = "testuser"
DUMMY_PASSWORD = "password123"

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["https://your-vercel-app.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Helper ---
def verify_dummy_user(x_dummy_user: str = Header(None)):
    """Check that the request contains a valid dummy username."""
    if not x_dummy_user or x_dummy_user != DUMMY_USERNAME:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid user")


@app.post("/upload/audio")
async def upload_audio(file: UploadFile = File(...), x_dummy_user: str = Header(None)):
    verify_dummy_user(x_dummy_user)

    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Invalid audio file")

    file_id = str(uuid4())
    filepath = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_audio(filepath)
    return JSONResponse(content={"file_id": file_id, "result": result})


@app.post("/upload/image")
async def upload_image(file: UploadFile = File(...), x_dummy_user: str = Header(None)):
    verify_dummy_user(x_dummy_user)

    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid image file")

    file_id = str(uuid4())
    filepath = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_image(filepath)
    return JSONResponse(content={"file_id": file_id, "caption": result})


@app.post("/upload/document")
async def upload_document(file: UploadFile = File(...), x_dummy_user: str = Header(None)):
    verify_dummy_user(x_dummy_user)

    if not (file.filename.endswith(".pdf") or file.filename.endswith(".docx")):
        raise HTTPException(status_code=400, detail="Only PDF/DOCX supported")

    file_id = str(uuid4())
    filepath = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_document(filepath)
    return JSONResponse(content={"file_id": file_id, "summary": result})

