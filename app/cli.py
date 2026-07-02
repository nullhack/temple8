from collections.abc import Sequence

from app.history import History, LookupRecord
from app.settings import Settings
from app.weather import WeatherAdapter


def main(argv: Sequence[str]) -> None:
    settings = Settings.from_env()
    adapter = WeatherAdapter(settings.geocoding_base, settings.forecast_base)
    history = History(settings.database_url)
    city = argv[0]
    conditions = adapter.forecast(adapter.geocode(city))
    history.record(
        LookupRecord(
            city=city,
            temperature=conditions.temperature,
            wind_speed=conditions.wind_speed,
            weather_code=conditions.weather_code,
        )
    )
    print(f"{city} {conditions.temperature}")
