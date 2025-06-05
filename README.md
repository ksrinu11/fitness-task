# Fitness Studio Booking API 🧘‍♀️🏃‍♂️

A production-style FastAPI service that lets clients **view classes** and **book spots** for a fictional fitness studio.  
Uses **SQLite** for persistence, stores datetimes in **UTC**, and converts on-the-fly to any IANA timezone.

---

## 📂  Project layout


---

## ⚡ Quick-start

### 1. Create a virtual-env & install deps

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn fitness_api.main:app --reload
uvicorn fitness_api.main:app --reload


Purpose	Method & Path	Complete URL
Swagger UI (interactive docs)	—	http://127.0.0.1:8000/docs
ReDoc docs	—	http://127.0.0.1:8000/redoc
List upcoming classes (default IST)	GET /classes	http://127.0.0.1:8000/classes
List classes in another zone (e.g. New York)	GET /classes?tz=America/New_York	http://127.0.0.1:8000/classes?tz=America/New_York
Book a class	POST /bookings	http://127.0.0.1:8000/bookings
All bookings for a client	GET /bookings?email=alice@example.com	http://127.0.0.1:8000/bookings?email=alice@example.com
Health check	GET /health	http://127.0.0.1:8000/health

---------post-------------

curl -X POST http://127.0.0.1:8000/bookings \
  -H "Content-Type: application/json" \
  -d '{
        "class_id": 1,
        "client_name": "Jane Doe",
        "client_email": "jane@example.com"
      }'
------------------windows---------------
# Build the JSON body
$body = @{
    class_id    = 1
    client_name = "Jane Doe"
    client_email= "jane@example.com"
} | ConvertTo-Json

# Send the POST request
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/bookings" `
  -Method Post `
  -Body $body `
  -ContentType "application/json"
