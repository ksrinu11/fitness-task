
from datetime import datetime
from fastapi import APIRouter

router = APIRouter(tags=["Utility"])

@router.get("/health")
def health():
    return {"status": "ok", "timestamp": datetime.utcnow()}
