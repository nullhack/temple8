GEOCODING_BASE: str
FORECAST_BASE: str
CASSETTE: str


def test_geocode_returns_coordinates_for_a_known_city() -> None: ...


def test_geocode_raises_for_an_unknown_city() -> None: ...


def test_forecast_returns_conditions_for_coordinates() -> None: ...
