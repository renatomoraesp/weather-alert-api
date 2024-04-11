from app.models.weather import Weather, Forecast
from app.utils.weather_utils import determine_safety_alert
from app.repositories.weather_repository import WeatherRepository

class WeatherServiceError(Exception):
    pass

class WeatherService:
    API_ENDPOINT = 'https://api.openweathermap.org/data/2.5'
    CURRENT_WEATHER_PATH = '/weather'
    FORECAST_PATH = '/forecast'
    HOURLY_PRECIPITATION_KEY = '1h'
    THREE_HOUR_PRECIPITATION_KEY = '3h'
    KELVIN_CONSTANT = 273.15

    def __init__(self, weather_repository: WeatherRepository):
        self.weather_repository = weather_repository

    def get_current_weather(self, city: str) -> Weather:
        data = self.weather_repository.get_current_weather(city)
        
        return self._parse_weather_data(data, city)

    def get_forecast(self, city: str) -> Forecast:
        data = self.weather_repository.get_forecast(city)
        forecast_data = [self._parse_weather_data(day, city, is_forecast=True) for day in data['list']]
        
        return Forecast(city=city, forecast=forecast_data)

    def _parse_weather_data(self, data: dict, city: str, is_forecast: bool = False) -> Weather:
        temperature_kelvin = self.__get_temperature_kelvin(data)
        temperature_fahrenheit = self.__kelvin_to_fahrenheit(temperature_kelvin)
        precipitation_key = self.__get_precipitation_key(is_forecast)

        precipitation = self.__get_precipitation(data, precipitation_key)
        wind_speed = self.__get_wind_speed(data)
        safety_alert = determine_safety_alert(temperature_fahrenheit, precipitation, wind_speed)
        
        return Weather(city=city, temperature=temperature_fahrenheit, precipitation=precipitation,
                       wind_speed=wind_speed, safety_alert=safety_alert)
    
    def __get_temperature_kelvin(self, data: dict) -> float:
        return data['main']['temp']
    
    def __kelvin_to_fahrenheit(self, kelvin):
        fahrenheit = (kelvin - self.KELVIN_CONSTANT) * 9/5 + 32
        
        return round(fahrenheit, 2)
    
    def __get_precipitation_key(self, is_forecast: bool) -> str:
        if is_forecast:
            return self.THREE_HOUR_PRECIPITATION_KEY
        
        return self.HOURLY_PRECIPITATION_KEY
    
    def __get_precipitation(self, data: dict, precipitation_key: str) -> float:
        return data.get('rain', {}).get(precipitation_key, 0)
    
    def __get_wind_speed(self, data: dict) -> float:
        return data['wind']['speed']