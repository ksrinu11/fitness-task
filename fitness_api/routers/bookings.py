
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..models import FitnessClass, Booking
from ..schemas import BookingCreate, BookingOut
from ..core.config import IST
from ..utils.timezone import get_timezone

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("", status_code=status.HTTP_201_CREATED, response_model=BookingOut)
def book_class(payload: BookingCreate, db: Session = Depends(get_db)):
    fc = db.query(FitnessClass).filter(FitnessClass.id == payload.class_id).first()
    if not fc:
        raise HTTPException(status_code=404, detail="Class not found")
    if fc.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")
    booking = Booking(
        class_id=fc.id,
        client_name=payload.client_name,
        client_email=payload.client_email,
    )
    fc.available_slots -= 1
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return BookingOut(
        id=booking.id,
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email,
        booked_at=booking.booked_at_utc.astimezone(IST),
        class_name=fc.name,
    )

@router.get("", response_model=List[BookingOut])
def get_bookings(
    email: str = Query(..., description="Client email used during booking"),
    tz: str = Query("Asia/Kolkata", description="IANA timezone, e.g. Europe/London"),
    db: Session = Depends(get_db),
):
    tz_obj = get_timezone(tz)
    bookings = db.query(Booking).filter(Booking.client_email == email).all()
    results = []
    for b in bookings:
        fc = db.query(FitnessClass).filter(FitnessClass.id == b.class_id).first()
        results.append(BookingOut(
            id=b.id,
            class_id=b.class_id,
            client_name=b.client_name,
            client_email=b.client_email,
            booked_at=b.booked_at_utc.astimezone(tz_obj),
            class_name=fc.name if fc else "[deleted]",
        ))
    return results
