# Weather Data Analyzer

Two command-line Python programs for cleaning daily weather data, calculating temperature and rainfall summaries, and displaying charts.

## Programs

- `project1.py` uses Pandas, NumPy, and Matplotlib for data cleaning, summary statistics, a temperature trend plot, and a rainfall bar chart.
- `project2.py` provides the same interactive workflow as a second implementation.

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

The programs also accept a CSV without a header row. The date is used as a label; temperature, humidity, and rainfall must be numeric. Missing temperatures and humidity values are filled with their respective column means, missing rainfall is treated as `0`, and duplicate rows are removed.

## Run

From this directory, run either program:

```powershell
python project1.py
```

or:

```powershell
python project2.py
```

Enter the CSV file path when prompted. Then choose from the interactive menu:

1. Print temperature statistics and total rainfall.
2. Print the cleaning report and display a temperature trend chart.
3. Display a daily rainfall chart.
4. Exit.

Matplotlib opens charts in a separate window. Close the chart window to return to the menu.
