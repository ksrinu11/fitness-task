
from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..models import FitnessClass
from ..schemas import ClassOut
from ..utils.timezone import get_timezone

router = APIRouter(prefix="/classes", tags=["Classes"])

@router.get("", response_model=List[ClassOut])
def list_classes(
    tz: str = Query("Asia/Kolkata", description="IANA timezone, e.g. America/New_York"),
    db: Session = Depends(get_db),
):
    tz_obj = get_timezone(tz)
    now_utc = datetime.utcnow()
    classes = db.query(FitnessClass).filter(FitnessClass.start_time_utc >= now_utc).all()
    return [
        ClassOut(
            id=c.id,
            name=c.name,
            start_time=c.start_time_utc.astimezone(tz_obj),
            instructor=c.instructor,
            available_slots=c.available_slots,
        )
        for c in classes
    ]
