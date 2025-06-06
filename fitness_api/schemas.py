
from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, Field

class ClassOut(BaseModel):
    id: int
    name: str
    start_time: datetime
    instructor: str
    available_slots: int

    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    class_id: int = Field(..., ge=1)
    client_name: str = Field(..., min_length=1)
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
    booked_at: datetime
    class_name: str

    class Config:
        orm_mode = True
