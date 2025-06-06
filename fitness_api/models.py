
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from .db.session import Base

class FitnessClass(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    start_time_utc = Column(DateTime, nullable=False)
    instructor = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    available_slots = Column(Integer, nullable=False)

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, nullable=False)
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)
    booked_at_utc = Column(DateTime, default=datetime.utcnow, nullable=False)
