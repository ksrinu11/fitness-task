
import pytz
from fastapi import HTTPException

def get_timezone(tz_str: str) -> pytz.timezone:
    try:
        return pytz.timezone(tz_str)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid timezone")
