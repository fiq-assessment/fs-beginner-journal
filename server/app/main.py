from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .core.db import init_db
from .routers import entries

app = FastAPI(
    title="Wellness Journal API",
    version="1.0.0",
    description="FS Beginner: Wellness Journal"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entries.router)

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/health")
async def health():
    return {"ok": True, "service": "wellness-journal-api"}

