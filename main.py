from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from livekit_server_route import router as livekit_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="LiveKit Token Service",
    description="Service for generating LiveKit access tokens",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(livekit_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok"}