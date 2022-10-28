import pytest
from app import app


test_json = {
        "reservation_status_date": "10/27/2015",
        "hotel": "Resort Hotel",
        "meal": "SC",
        "market_segment": "Direct",
        "distribution_channel": "Direct",
        "reserved_room_type": "E",
        "deposit_type": "Refundable",
        "customer_type": "Transient",
        "lead_time": 457,
        "arrival_date_week_number": 43,
        "arrival_date_day_of_month": 10,
        "stays_in_weekend_nights": 2,
        "stays_in_week_nights": 2,
        "adults": 2,
        "children": 0,
        "babies": 0,
        "is_repeated_guest": 0,
        "previous_cancellations": 0,
        "previous_bookings_not_canceled": 1,
        "required_car_parking_spaces": 0,
        "total_of_special_requests": 0,
        "agent": 8,
        "company": 110,
        "adr": 120,
        "days_in_waiting_list": 0,
        "arrival_date_year": 2015,
        "assigned_room_type": "C",
        "booking_changes": 3,
        "reservation_status": "Check-Out",
        "country": "PRT",
        "arrival_date_month": "October",
        "is_canceled": 0
    }


@pytest.fixture
def client():
    return app.test_client()


def test_predict_valid_registry(client):
    response = client.get('/model/predict', json=test_json)
    assert response.status_code == 200
