from typing import Any

import pytest

CASSETTE = "tests/cassettes/open-meteo/open-meteo.yaml"


@pytest.mark.pending
def test_cli_prints_current_conditions_for_a_city(capsys: Any, monkeypatch: Any) -> None:
    import vcr

    from app.cli import main

    monkeypatch.setenv("WEATHER_GEOCODING_BASE", "https://geocoding-api.open-meteo.com")
    monkeypatch.setenv("WEATHER_FORECAST_BASE", "https://api.open-meteo.com")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")

    with vcr.use_cassette(CASSETTE):
        main(["Berlin"])

    out = capsys.readouterr().out
    assert "Berlin" in out
    assert "16.1" in out
