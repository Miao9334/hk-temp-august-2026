# Process

## Tools

I used Gemini to help draft, debug, inspect dataset links, and optimize scripts for Assignment 2 (`fetch.py` and `plot.py`).

## Kept

- **Open-Meteo Historical Weather API Integration**: I kept the direct API integration in `fetch.py` fetching 2026 August hourly temperature data using Open-Meteo (`https://open-meteo.com`), ensuring a working, non-404 data source link.
- **Explicit Timezone Handling (`Asia/Hong_Kong`)**: I retained the `timezone=Asia%2FHong_Kong` parameter in the API request URL to ensure all hourly timestamps strictly align with Hong Kong local time.
- **Warm Color Palette (`OrRd`)**: I kept the updated warm colormap (`OrRd`) in `plot.py` to represent lower temperatures in light orange instead of blue, better capturing the tropical summer atmosphere of Hong Kong.

## Rejected

- **Hardcoded Local/Synthetic Data Generation**: Initially, `fetch.py` relied on synthetic data generation. I rejected this approach after identifying that Open-Meteo provides actual historical weather records, switching to direct API fetching.
- **Data Source Links with 404 Errors**: I rejected invalid dataset paths from the HK Open Data portal that produced `404 Not Found` errors, replacing them with the valid Open-Meteo endpoint URL.
- **Default UTC Timezone Data**: The initial API call returned hourly data in UTC, which placed peak temperatures around 04:00-08:00 AM local time. I rejected UTC timestamps and required explicit local HKT conversion.
- **Diverging Blue-Red Colormap (`RdBu`)**: I rejected the default `RdBu` palette because the cool blue hues incorrectly implied freezing or cold conditions for a tropical 24°C summer morning.