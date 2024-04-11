import os
from dotenv import load_dotenv

class Config:
    load_dotenv()
    API_KEY = os.getenv('WEATHER_API_KEY')