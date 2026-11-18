"""
Weather Data Analyzer
Author: Manas Singh

A beginner-friendly command-line project that reads weather data from a CSV,
cleans it, calculates statistics, and displays charts.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


REQUIRED_COLUMNS = ["Date", "Temp", "Humidity", "Rainfall"]


def load_weather_data(file_name):
    """Load a CSV file and check that it has the required columns."""
    if not os.path.isfile(file_name):
        print(f"Error: File '{file_name}' not found. Please enter a valid file name.")
        return None

    try:
        data = pd.read_csv(file_name)
    except Exception as error:
        print("Error: Could not read the CSV file.")
        print("Details:", error)
        return None

    # Ignore differences in capitalization and extra spaces in column names.
    data.columns = [str(column).strip().title() for column in data.columns]

    missing_columns = []
    for column in REQUIRED_COLUMNS:
        if column not in data.columns:
            missing_columns.append(column)

    if missing_columns:
        print("Error: Missing required column(s):", ", ".join(missing_columns))
        print("Required columns:", ", ".join(REQUIRED_COLUMNS))
        return None

    return data[REQUIRED_COLUMNS].copy()


def clean_weather_data(data):
    """Remove duplicate rows and handle missing or invalid values."""
    original_count = len(data)

    # Convert values to the correct data types.
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    for column in ["Temp", "Humidity", "Rainfall"]:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # A row without a valid date cannot be used in a date-based analysis.
    data = data.dropna(subset=["Date"])

    # Remove exact duplicate records.
    before_duplicates = len(data)
    data = data.drop_duplicates()
    duplicates_removed = before_duplicates - len(data)

    # Fill missing numeric values with that column's mean.
    # If a complete column has no valid values, use 0 so the program can continue.
    for column in ["Temp", "Humidity", "Rainfall"]:
        if data[column].isna().any():
            column_mean = data[column].mean()
            if pd.isna(column_mean):
                column_mean = 0
            data[column] = data[column].fillna(column_mean)

    data = data.sort_values("Date").reset_index(drop=True)

    return data, original_count, duplicates_removed


def show_summary(data):
    """Display a short data summary and weather statistics."""
    if data.empty:
        print("No valid weather records are available.")
        return

    temperatures = data["Temp"].to_numpy()
    rainfall = data["Rainfall"].to_numpy()

    average_temp = np.mean(temperatures)
    maximum_temp = np.max(temperatures)
    minimum_temp = np.min(temperatures)
    standard_deviation = np.std(temperatures)
    total_rainfall = np.sum(rainfall)

    max_index = data["Temp"].idxmax()
    min_index = data["Temp"].idxmin()
    max_date = data.loc[max_index, "Date"].strftime("%Y-%m-%d")
    min_date = data.loc[min_index, "Date"].strftime("%Y-%m-%d")

    print("\n========== WEATHER DATA SUMMARY ==========")
    print("Number of records :", len(data))
    print("Date range        :", data["Date"].min().strftime("%Y-%m-%d"),
          "to", data["Date"].max().strftime("%Y-%m-%d"))
    print("Average humidity  :", f"{data['Humidity'].mean():.2f}%")
    print("Average rainfall  :", f"{data['Rainfall'].mean():.2f} mm")
    print("------------------------------------------")
    print(f"Average Temp: {average_temp:.2f} C")
    print(f"Max: {maximum_temp:g} ({max_date})")
    print(f"Min: {minimum_temp:g} ({min_date})")
    print(f"Std Dev: {standard_deviation:.2f}")
    print(f"Total Rainfall: {total_rainfall:g} mm")
    print("==========================================\n")


def plot_weather_data(data):
    """Display a temperature line chart and a rainfall bar chart."""
    if data.empty:
        print("There is no data to plot.")
        return

    dates = data["Date"].dt.strftime("%Y-%m-%d")

    # Chart 1: Temperature trend.
    plt.figure(figsize=(9, 5))
    plt.plot(dates, data["Temp"], marker="o", linewidth=2)
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Chart 2: Daily rainfall.
    plt.figure(figsize=(9, 5))
    plt.bar(dates, data["Rainfall"])
    plt.title("Daily Rainfall")
    plt.xlabel("Date")
    plt.ylabel("Rainfall (mm)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


def main():
    """Run the menu-driven Weather Data Analyzer."""
    print("===================================")
    print("       WEATHER DATA ANALYZER")
    print("          Author: Manas Singh")
    print("===================================")

    file_name = input("Enter CSV file name (example: weather.csv): ").strip()
    data = load_weather_data(file_name)

    if data is None:
        return

    print("\nCSV file loaded successfully.")
    print("\nOriginal data preview:")
    print(data.head())
    print("\nOriginal data information:")
    print("Rows:", len(data))
    print("Missing values in each column:")
    print(data.isna().sum())

    cleaned_data, original_count, duplicates_removed = clean_weather_data(data)

    print("\nData cleaning completed.")
    print("Original rows     :", original_count)
    print("Duplicates removed:", duplicates_removed)
    print("Cleaned rows      :", len(cleaned_data))

    while True:
        print("\n-------------- MENU --------------")
        print("1. Show Weather Summary")
        print("2. Clean Data and Plot Charts")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            show_summary(cleaned_data)

        elif choice == "2":
            print("\nCleaned data:")
            print(cleaned_data.to_string(index=False))
            print("\nDisplaying Temperature Trend and Daily Rainfall charts...")
            plot_weather_data(cleaned_data)

        elif choice == "3":
            print("Thank you for using Weather Data Analyzer!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
