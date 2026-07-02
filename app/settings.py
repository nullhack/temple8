import os
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class Settings:
    geocoding_base: str
    forecast_base: str
    database_url: str

    @classmethod
    def from_env(cls) -> Self:
        return cls(
            geocoding_base=os.environ.get(
                "WEATHER_GEOCODING_BASE", "https://geocoding-api.open-meteo.com"
            ),
            forecast_base=os.environ.get(
                "WEATHER_FORECAST_BASE", "https://api.open-meteo.com"
            ),
            database_url=os.environ.get("DATABASE_URL", "sqlite:///weather.db"),
        )
