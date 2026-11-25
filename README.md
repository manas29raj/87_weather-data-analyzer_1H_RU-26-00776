# 🌦️ Weather Data Analyzer

A simple, menu-driven Python project that reads daily weather records from a CSV file, cleans the data, calculates useful statistics, and visualizes temperature and rainfall trends.

> **Project No.:** 87  
> **Author:** Manas Singh  
> **Language:** Python 3.15.2

## ✨ Features

- Loads weather records from a CSV file using **Pandas**.
- Displays a preview, row count, and missing-value summary.
- Removes duplicate records.
- Converts invalid numeric values to missing values and fills missing numeric values with the column mean.
- Uses **NumPy** to calculate:
  - Average temperature
  - Maximum and minimum temperature
  - Temperature standard deviation
  - Total rainfall
- Uses **Matplotlib** to display:
  - A temperature trend line chart
  - A daily rainfall bar chart
- Provides a simple console menu.

## 🧰 Technologies

Only the libraries specified in the project statement are used:

| Library | Purpose |
|---|---|
| Pandas | Read CSV files and clean tabular data |
| NumPy | Perform numerical calculations |
| Matplotlib | Create charts |

The remaining code uses Python's built-in modules and features. No additional third-party libraries are required.

## 📁 Project Structure

```text
Weather-Data-Analyzer/
│
├── main.py
├── weather.csv
├── requirements.txt
└── README.md
```

## ⚙️ Setup

### 1. Install Python

Install Python 3 if it is not already installed.

### 2. Install the required libraries

Open a terminal in the project folder and run:


```bash
pip install pandas numpy matplotlib
```

### 3. Run the program

```bash
python main.py
```

When prompted for the CSV file name, enter:

```text
weather.csv
```

Keep `weather.csv` in the same folder as `main.py`, or enter the full path to your CSV file.

## 🗂️ CSV Format

The CSV file must contain these four columns:

| Column | Description | Example |
|---|---|---|
| `Date` | Date of the weather record | `2026-08-01` |
| `Temp` | Temperature in Celsius | `32` |
| `Humidity` | Humidity percentage | `70` |
| `Rainfall` | Rainfall in millimetres | `0` |

Example:

```csv
Date,Temp,Humidity,Rainfall
2026-08-01,32,70,0
2026-08-02,34,65,0
2026-08-03,30,80,12
```

Column names are case-insensitive after trimming surrounding spaces. The required columns must still be present.

## 🕹️ Menu Options

| Option | Action |
|---|---|
| `1` | Display the weather summary and calculated statistics |
| `2` | Display cleaned data and open both charts |
| `3` | Exit the program |

## 🧹 Data Cleaning Rules

1. Dates are converted to date values. Rows with invalid or missing dates are removed because they cannot be used in date-based analysis.
2. Temperature, humidity, and rainfall are converted to numeric values. Invalid numeric entries become missing values.
3. Exact duplicate records are removed.
4. Missing numeric values are filled using the mean of their respective columns. If an entire numeric column has no valid values, its missing values are filled with `0`.
5. The cleaned records are sorted by date.

## 📊 Expected Output Example

For the sample `weather.csv`, choosing option `1` produces these key results:

```text
Average Temp: 32.00 C
Max: 34 (2026-08-02)
Min: 30 (2026-08-03)
Std Dev: 1.63
Total Rainfall: 12 mm
```

Choosing option `2` displays the cleaned records and opens two Matplotlib windows: **Temperature Trend** and **Daily Rainfall**.

## 🧪 Test Scenarios

| Test case | Input / situation | Expected behavior |
|---|---|---|
| 1. Normal input | Three valid weather records | Correct average, maximum, minimum, and total rainfall |
| 2. Minimum input | A CSV containing one valid row | Statistics are calculated; standard deviation is `0.00` |
| 3. Invalid input | CSV file does not exist | A clear file-not-found error is displayed |
| 4. Different valid scenario | Duplicate row and missing temperature | Duplicate is removed and missing temperature is filled with the column mean |

For Test Case 4, use this CSV content:

```csv
Date,Temp,Humidity,Rainfall
2026-08-01,32,70,0
2026-08-02,,65,0
2026-08-02,,65,0
2026-08-03,30,80,12
```

The duplicate row is removed first. The remaining missing temperature is filled with the mean of the available temperatures: `(32 + 30) / 2 = 31`.

## 📝 Notes

- Standard deviation is calculated using NumPy's default population standard deviation (`numpy.std`).
- The program expects the CSV header names `Date`, `Temp`, `Humidity`, and `Rainfall`.
- Charts open in separate Matplotlib windows. Close the chart windows to return to the menu.
- The sample CSV is included so the project can be tested immediately.

## 👨‍💻 Author

**Manas Singh**

---

*Built as a Python data analysis project.*
