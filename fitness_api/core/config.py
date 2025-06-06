
from pathlib import Path
import pytz

# SQLite DB in project directory
DATABASE_URL = f"sqlite:///{Path(__file__).resolve().parent.parent}/fitness.db"

# Default studio timezone (IST)
IST = pytz.timezone("Asia/Kolkata")
