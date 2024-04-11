from dataclasses import dataclass
from typing import List

@dataclass
class Weather:
    city: str
    temperature: float
    precipitation: float
    wind_speed: float
    safety_alert: str

@dataclass
class Forecast:
    city: str
    forecast: List[Weather]