from flask import Blueprint, jsonify, abort
from app.services.weather_service import WeatherService, WeatherServiceError
from app.repositories.weather_repository import WeatherRepository
from app.config import Config

weather_controller = Blueprint('weather', __name__)
weather_repository = WeatherRepository(Config.API_KEY)
weather_service = WeatherService(weather_repository)

@weather_controller.route('/weather/<city>')
def get_weather(city):
    try:
        weather_data = weather_service.get_current_weather(city)
        return jsonify(weather_data.__dict__)
    except WeatherServiceError as e:
        abort(500, description=str(e))

@weather_controller.route('/forecast/<city>')
def get_forecast(city):
    try:
        forecast_data = weather_service.get_forecast(city)
        return jsonify(forecast_data.__dict__)
    except WeatherServiceError as e:
        abort(500, description=str(e))