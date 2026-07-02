# Glossary: temple8

> The ubiquitous language for this project — terms shared across conversation,
> code, and documentation (Evans, 2003). Curated from the interview for the
> IMPORTANT domain concepts, not every code symbol. Grouped by bounded context,
> where each term has one meaning. The tests are the source of truth for
> behaviour; this glossary is the source of truth for names. Extend or revise
> entries as understanding shifts.

## Context: weather-lookup

### City
A place name that the user supplies as the lookup target, resolved to
coordinates through the geocoding service.
*Aliases: none · Source: weather lookup*

### Coordinates
A geographic position that the geocoding service returns for a city, carrying
the latitude and longitude the forecast service needs.
*Aliases: lat/lon · Source: weather lookup*

### Conditions
A snapshot of the current weather at a coordinate — temperature, wind speed,
and weather code — produced by the forecast service.
*Aliases: current weather · Source: weather lookup*

### WeatherAdapter
An anti-corruption layer that translates the open-meteo geocoding and forecast
endpoints into the domain's `Coordinates` and `Conditions` types.
*Aliases: none · Source: weather lookup*

## Context: history

### Lookup
A single completed weather check — the city asked, the conditions returned, and
the time it was recorded — stored as one entry in the history.
*Aliases: LookupRecord · Source: weather lookup*

### History
An ordered, latest-first log of past lookups that the system appends to on each
check and recalls on demand.
*Aliases: lookup log · Source: weather lookup*
