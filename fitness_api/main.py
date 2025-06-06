
from fastapi import FastAPI
from .db.session import Base, engine, SessionLocal
from .seed import seed_classes
from .routers import classes, bookings, health

# Create DB tables
Base.metadata.create_all(bind=engine)

# Seed initial data
with SessionLocal() as session:
    seed_classes(session)

app = FastAPI(title="Fitness Studio Booking API", version="2.0.0")

# Register routers
app.include_router(classes.router)
app.include_router(bookings.router)
app.include_router(health.router)
