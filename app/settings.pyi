from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class Settings:
    geocoding_base: str
    forecast_base: str
    database_url: str

    @classmethod
    def from_env(cls) -> Self: ...
