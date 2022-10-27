import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_fit(client):
    response = client.get('/model/fit')
    assert response.status_code == 200