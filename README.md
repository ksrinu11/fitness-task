
# Fitness Studio Booking API (Modular Version)

This version refactors the original single-file demo into a cleaner Python package **`fitness_api`** and adds a minimal Pytest suite.

## 📦 Project layout

```
fitness_api/
    core/config.py           # global settings
    db/session.py            # engine & session
    models.py                # ORM tables
    schemas.py               # Pydantic models
    seed.py                  # initial data
    routers/                 # route modules
    utils/timezone.py        # timezone helper
    main.py                  # FastAPI app
tests/
    test_api.py              # quick smoke tests
```

## 🛠️ Setup & Run

```bash
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn fitness_api.main:app --reload
```

Swagger docs at `http://127.0.0.1:8000/docs`.

## 🧪 Run Tests

```bash
pytest -q
```

The tests spin up the app with **TestClient**, verify `/classes` returns seed data and that booking endpoint works end‑to‑end.

## 📋 Endpoints

* `GET /classes?tz=America/New_York` – list upcoming classes in any timezone.
* `POST /bookings` – book a spot:
  ```json
  {
    "class_id": 1,
    "client_name": "Alice",
    "client_email": "alice@example.com"
  }
  ```
* `GET /bookings?email=alice@example.com` – all bookings for a user.
* `GET /health` – simple health probe.

Happy coding! 🎉
