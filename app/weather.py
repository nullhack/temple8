import httpx
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
    def __init__(self, geocoding_base: str, forecast_base: str) -> None:
        self._geocoding_base = geocoding_base
        self._forecast_base = forecast_base
        self._client = httpx.Client()

    def geocode(self, city: str) -> Coordinates:
        response = self._client.get(
            f"{self._geocoding_base}/v1/search",
            params={"name": city, "count": 1, "language": "en", "format": "json"},
        )
        response.raise_for_status()
        results = response.json().get("results")
        if not results:
            raise LookupError(city)
        hit = results[0]
        return Coordinates(latitude=hit["latitude"], longitude=hit["longitude"])

    def forecast(self, coordinates: Coordinates) -> Conditions:
        response = self._client.get(
            f"{self._forecast_base}/v1/forecast",
            params={
                "latitude": coordinates.latitude,
                "longitude": coordinates.longitude,
                "current": "temperature_2m,wind_speed_10m,weather_code",
            },
        )
        response.raise_for_status()
        current = response.json()["current"]
        return Conditions(
            temperature=current["temperature_2m"],
            wind_speed=current["wind_speed_10m"],
            weather_code=current["weather_code"],
        )
