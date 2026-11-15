# Weather Data Analyzer

`project2.py` is a command-line Python program for cleaning daily weather data, calculating temperature and rainfall summaries, and displaying charts.

## Features

- Removes duplicate rows and fills missing temperature and humidity values with their column means.
- Treats missing rainfall values as `0`.
- Prints temperature statistics and total rainfall.
- Displays temperature trend and daily rainfall charts.

## Requirements

- Python 3.9 or later
- The packages listed in `requirements.txt`

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Input CSV format

When prompted, enter the path to a CSV file with four fields per row, in this order:

```csv
Date,Temp,Humidity,Rainfall
2026-01-01,18.5,65,0
2026-01-02,20.0,58,1.2
```

The CSV may include a header row or omit it. The date is used as a label; temperature, humidity, and rainfall must be numeric. Missing temperatures and humidity values are filled with their respective column means, missing rainfall is treated as `0`, and duplicate rows are removed.

## Run

From this directory, run the program:

```powershell
python project2.py
```

Enter the CSV file path when prompted. Then choose from the interactive menu:

1. Print temperature statistics and total rainfall.
2. Print the cleaning report and display a temperature trend chart.
3. Display a daily rainfall chart.
4. Exit.

Matplotlib opens charts in a separate window. Close the chart window to return to the menu.
