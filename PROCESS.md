# Process

## Tools

I used Gemini to help draft, debug, and optimize the scripts for Assignment 2 (`fetch.py` and `plot.py`).

## Kept

- **Offline Raw Data Handling Logic**: I kept the conditional logic in `fetch.py` that verifies whether the dataset already exists locally before attempting any operations, fully adhering to the assignment's offline requirement.
- **Heatmap Visualization via Seaborn/Matplotlib**: I kept the implementation in `plot.py` using `seaborn.heatmap` and `pandas.pivot` to transform daily and hourly temperature records into a clean 2D grid matrix (Day vs. Hour) for proper visualization.

## Rejected

- **Online Remote HTTP Fetching**: The initial AI-generated script attempted live HTTP network requests via `requests.get` to remote Open Data URLs, which returned `HTTP 404 Not Found` errors due to missing/non-existent future endpoints. I rejected making online HTTP requests during script execution and switched to the offline file-checking rule.
- **Single-Line Plot Rendering**: The AI initially produced code for a basic 1D line chart. I rejected this structure because the assignment required visualizing multi-dimensional hourly grid trends, requiring a transposed 2D heatmap matrix instead.