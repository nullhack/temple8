from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float


@dataclass(frozen=True)
class Conditions:
    temperature: float
    wind_speed: float
    weather_code: int


class WeatherAdapter:
    def __init__(self, geocoding_base: str, forecast_base: str) -> None: ...
    def geocode(self, city: str) -> Coordinates: ...
    def forecast(self, coordinates: Coordinates) -> Conditions: ...
