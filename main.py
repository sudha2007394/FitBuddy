from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from app.routes import router
from app.database import init_db
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
init_db()
app.include_router(router)

BASE_DIR = Path(__file__).resolve().parent.parent
possible_paths = [
    BASE_DIR / "frontend" / "index.html",
    BASE_DIR / "app" / "frontend" / "index.html",
    BASE_DIR / "index.html",
]
INDEX_PATH = None
for p in possible_paths:
    if p.exists():
        INDEX_PATH = p
        break

@app.get("/")
def home():
    if INDEX_PATH:
        return FileResponse(INDEX_PATH)
    return HTMLResponse("<h1>Backend Running da!</h1>")

@app.get("/health")
def health():
    return {"status": "ok"}