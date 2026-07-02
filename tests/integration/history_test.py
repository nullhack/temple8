from typing import Any

import pytest


@pytest.mark.pending
def test_record_stores_a_lookup_and_recent_returns_it(tmp_path: Any) -> None:
    from app.history import History, LookupRecord

    history = History(f"sqlite:///{tmp_path / 'weather.db'}")
    history.record(
        LookupRecord(city="Berlin", temperature=16.2, wind_speed=6.5, weather_code=0)
    )

    recent = history.recent()

    assert len(recent) == 1
    assert recent[0].city == "Berlin"


@pytest.mark.pending
def test_recent_returns_lookups_latest_first(tmp_path: Any) -> None:
    from app.history import History, LookupRecord

    history = History(f"sqlite:///{tmp_path / 'weather.db'}")
    history.record(
        LookupRecord(city="Berlin", temperature=16.2, wind_speed=6.5, weather_code=0)
    )
    history.record(
        LookupRecord(city="Paris", temperature=20.0, wind_speed=5.0, weather_code=1)
    )

    recent = history.recent()

    assert [r.city for r in recent] == ["Paris", "Berlin"]


@pytest.mark.pending
def test_recent_returns_empty_list_when_none_recorded(tmp_path: Any) -> None:
    from app.history import History

    history = History(f"sqlite:///{tmp_path / 'weather.db'}")

    assert history.recent() == []
