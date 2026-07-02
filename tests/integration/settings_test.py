from typing import Any


def test_from_env_reads_api_bases_and_database_url(monkeypatch: Any) -> None:
    from app.settings import Settings

    monkeypatch.setenv("WEATHER_GEOCODING_BASE", "https://geo.example.com")
    monkeypatch.setenv("WEATHER_FORECAST_BASE", "https://forecast.example.com")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///tmp/test.db")

    settings = Settings.from_env()

    assert settings.geocoding_base == "https://geo.example.com"
    assert settings.forecast_base == "https://forecast.example.com"
    assert settings.database_url == "sqlite:///tmp/test.db"


def test_from_env_applies_defaults_when_env_unset(monkeypatch: Any) -> None:
    from app.settings import Settings

    monkeypatch.delenv("WEATHER_GEOCODING_BASE", raising=False)
    monkeypatch.delenv("WEATHER_FORECAST_BASE", raising=False)
    monkeypatch.delenv("DATABASE_URL", raising=False)

    settings = Settings.from_env()

    assert settings.geocoding_base == "https://geocoding-api.open-meteo.com"
    assert settings.forecast_base == "https://api.open-meteo.com"
    assert settings.database_url == "sqlite:///weather.db"
