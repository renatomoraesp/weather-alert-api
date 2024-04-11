import requests

class WeatherRepository:
    API_ENDPOINT = 'https://api.openweathermap.org/data/2.5'
    CURRENT_WEATHER_PATH = '/weather'
    FORECAST_PATH = '/forecast'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_current_weather(self, city: str) -> dict:
        return self._make_api_request(self.CURRENT_WEATHER_PATH, {'q': city})

    def get_forecast(self, city: str) -> dict:
        return self._make_api_request(self.FORECAST_PATH, {'q': city})

    def _make_api_request(self, path: str, params: dict) -> dict:
        url = f'{self.API_ENDPOINT}{path}'
        params['appid'] = self.api_key
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        return response.json()