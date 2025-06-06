
from datetime import datetime
import pytz
from sqlalchemy.orm import Session
from .models import FitnessClass
from .core.config import IST
def seed_classes(db: Session):
    if db.query(FitnessClass).count() > 0:
        return
    seeds = [
        {"name": "Yoga", "local_dt": datetime(2025, 6, 7, 7, 0)},
        {"name": "Zumba", "local_dt": datetime(2025, 6, 7, 9, 0)},
        {"name": "HIIT", "local_dt": datetime(2025, 6, 7, 18, 0)},
    ]
    for s in seeds:
        utc_dt = IST.localize(s["local_dt"]).astimezone(pytz.utc)
        db.add(FitnessClass(
            name=s["name"],
            start_time_utc=utc_dt,
            instructor=f"Coach {s['name']}",
            capacity=20,
            available_slots=20,
        ))
    db.commit()
