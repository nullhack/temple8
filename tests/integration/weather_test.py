import pytest

GEOCODING_BASE = "https://geocoding-api.open-meteo.com"
FORECAST_BASE = "https://api.open-meteo.com"
CASSETTE = "tests/cassettes/open-meteo/open-meteo.yaml"


def test_geocode_returns_coordinates_for_a_known_city() -> None:
    import vcr

    from app.weather import WeatherAdapter

    adapter = WeatherAdapter(GEOCODING_BASE, FORECAST_BASE)
    with vcr.use_cassette(CASSETTE):
        coordinates = adapter.geocode("Berlin")

    assert coordinates.latitude == pytest.approx(52.52437)
    assert coordinates.longitude == pytest.approx(13.41053)


def test_geocode_raises_for_an_unknown_city() -> None:
    import vcr

    from app.weather import WeatherAdapter

    adapter = WeatherAdapter(GEOCODING_BASE, FORECAST_BASE)
    with vcr.use_cassette(CASSETTE), pytest.raises(LookupError):
        adapter.geocode("Xyzqwerty")


def test_forecast_returns_conditions_for_coordinates() -> None:
    import vcr

    from app.weather import Coordinates, WeatherAdapter

    adapter = WeatherAdapter(GEOCODING_BASE, FORECAST_BASE)
    with vcr.use_cassette(CASSETTE):
        conditions = adapter.forecast(Coordinates(52.52437, 13.41053))

    assert conditions.temperature == pytest.approx(16.1)
    assert conditions.wind_speed == pytest.approx(6.5)
    assert conditions.weather_code == 0
