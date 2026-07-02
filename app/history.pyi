from dataclasses import dataclass


@dataclass(frozen=True)
class LookupRecord:
    city: str
    temperature: float
    wind_speed: float
    weather_code: int


class History:
    def __init__(self, database_url: str) -> None: ...
    def record(self, lookup: LookupRecord) -> None: ...
    def recent(self) -> list[LookupRecord]: ...
