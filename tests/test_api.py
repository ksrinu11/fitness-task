
from fastapi.testclient import TestClient
from fitness_api.main import app

client = TestClient(app)

def test_list_classes():
    resp = client.get("/classes")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list) and len(data) >= 3
    assert all("available_slots" in c for c in data)

def test_booking_flow():
    # book first class
    booking_payload = {
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "test@example.com"
    }
    resp = client.post("/bookings", json=booking_payload)  # router prefix /bookings acts as POST for booking
    # Actually booking endpoint is POST /bookings
    assert resp.status_code == 201
    booking = resp.json()
    assert booking["client_email"] == "test@example.com"

    # list bookings
    resp2 = client.get("/bookings", params={"email": "test@example.com"})
    assert resp2.status_code == 200
    user_bookings = resp2.json()
    assert len(user_bookings) >= 1
