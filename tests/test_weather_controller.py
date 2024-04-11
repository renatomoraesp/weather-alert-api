import pytest
from app import create_app
from flask import json

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_weather(client):
    response = client.get('/weather/New%20York')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'city' in data
    assert 'temperature' in data
    assert 'precipitation' in data
    assert 'wind_speed' in data
    assert 'safety_alert' in data

def test_get_forecast(client):
    response = client.get('/forecast/New%20York')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'city' in data
    assert 'forecast' in data
    assert isinstance(data['forecast'], list)
    if data['forecast']:
        forecast_item = data['forecast'][0]
        assert 'city' in forecast_item
        assert 'temperature' in forecast_item
        assert 'precipitation' in forecast_item
        assert 'wind_speed' in forecast_item
        assert 'safety_alert' in forecast_item