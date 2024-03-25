import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"USD to INR Converter" in response.data

def test_convert_usd_to_inr():
    amount = '10'
    converted_amount = app.convert_usd_to_inr(amount)
    assert isinstance(converted_amount, float)
