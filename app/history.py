import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class LookupRecord:
    city: str
    temperature: float
    wind_speed: float
    weather_code: int


class History:
    def __init__(self, database_url: str) -> None:
        path = database_url.removeprefix("sqlite:///")
        self._connection = sqlite3.connect(path)
        self._connection.execute(
            "CREATE TABLE IF NOT EXISTS lookups"
            " (id INTEGER PRIMARY KEY AUTOINCREMENT,"
            " city TEXT, temperature REAL, wind_speed REAL, weather_code INTEGER)"
        )
        self._connection.commit()

    def record(self, lookup: LookupRecord) -> None:
        self._connection.execute(
            "INSERT INTO lookups (city, temperature, wind_speed, weather_code)"
            " VALUES (?, ?, ?, ?)",
            (lookup.city, lookup.temperature, lookup.wind_speed, lookup.weather_code),
        )
        self._connection.commit()

    def recent(self) -> list[LookupRecord]:
        rows = self._connection.execute(
            "SELECT city, temperature, wind_speed, weather_code"
            " FROM lookups ORDER BY id DESC"
        ).fetchall()
        return [
            LookupRecord(
                city=row[0],
                temperature=row[1],
                wind_speed=row[2],
                weather_code=row[3],
            )
            for row in rows
        ]
