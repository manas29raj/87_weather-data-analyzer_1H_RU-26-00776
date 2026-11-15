# Weather Data Analyzer
# Reads daily weather data from a CSV file, cleans it, and displays summaries and charts.

import numpy as np                  # Calculates statistics such as means and extrema
import pandas as pd                  # Loads and cleans tabular CSV data
import matplotlib.pyplot as plt      # Creates the weather charts

COLUMNS = ["Date", "Temp", "Humidity", "Rainfall"]  # Expected CSV fields, in order


def load_data():
    """Prompt for a CSV file and load it using the expected column names."""
    while True:  # Keep prompting until the file can be opened
        file_name = input("Enter CSV file name: ").strip()
        try:
            # The input may include a header row; clean_data removes it if present.
            return pd.read_csv(file_name, header=None, names=COLUMNS)
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found. Please enter a valid file name.")


def clean_data(df):
    """Remove duplicate rows and fill missing measurements."""
    # Remove a CSV header that pandas initially read as a data row.
    df = df[df["Date"] != "Date"].copy()

    # Convert measurements to numbers; invalid or blank values become NaN.
    for column in ["Temp", "Humidity", "Rainfall"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    rows_before = len(df)
    df = df.drop_duplicates()  # Remove exact duplicate records
    duplicates_removed = rows_before - len(df)

    # Use each measurement's mean to fill missing temperature and humidity.
    temp_mean = np.mean(df["Temp"].dropna())
    humidity_mean = np.mean(df["Humidity"].dropna())
    df["Temp"] = df["Temp"].fillna(temp_mean)
    df["Humidity"] = df["Humidity"].fillna(humidity_mean)
    df["Rainfall"] = df["Rainfall"].fillna(0)  # Treat missing rainfall as no rain

    # Return a clean, sequential index along with the cleaning report values.
    return df.reset_index(drop=True), duplicates_removed, temp_mean


def show_summary(df):
    """Print temperature statistics and total rainfall."""
    temps = df["Temp"].to_numpy()  # NumPy array used for the statistics below
    average = np.mean(temps)
    max_temp = np.max(temps)
    min_temp = np.min(temps)
    std_dev = np.std(temps)

    if len(df) == 1:  # A single record has no hottest/coldest date comparison.
        print(
            f"Average Temp: {average:.2f} C | Max: {max_temp:g} | "
            f"Min: {min_temp:g} | Std Dev: {std_dev:.2f}"
        )
        return

    hottest_date = df["Date"].iloc[np.argmax(temps)]
    coldest_date = df["Date"].iloc[np.argmin(temps)]
    total_rain = np.sum(df["Rainfall"].to_numpy())
    print(
        f"Average Temp: {average:.2f} C | Max: {max_temp:g} ({hottest_date}) | "
        f"Min: {min_temp:g} ({coldest_date}) | Std Dev: {std_dev:.2f} | "
        f"Total Rainfall: {total_rain:.2f} mm"
    )


def clean_and_plot(df, duplicates_removed, temp_mean):
    """Print a cleaning report and display a temperature trend chart."""
    print(
        f"Duplicates removed: {duplicates_removed} | "
        f"Missing Temp filled with mean: {temp_mean:.2f}"
    )
    print(f"Cleaned rows: {len(df)} | Line chart 'Temperature Trend' displayed")

    # Plot temperature values against their date labels.
    plt.figure()
    plt.plot(df["Date"], df["Temp"], marker="o")
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.xticks(rotation=30)  # Rotate labels so dates are easier to read
    plt.tight_layout()
    plt.show()


def rainfall_bar_chart(df):
    """Display a bar chart of daily rainfall."""
    plt.figure()
    plt.bar(df["Date"], df["Rainfall"])
    plt.title("Rainfall Bar Chart")
    plt.xlabel("Date")
    plt.ylabel("Rainfall (mm)")
    plt.xticks(rotation=30)
    plt.tight_layout()  # Keep labels and chart elements within the figure
    plt.show()


def main():
    """Load and clean weather data, then run the interactive menu."""
    raw = load_data()
    print(f"Loaded {len(raw)} rows, columns: {', '.join(COLUMNS)}")
    df, duplicates_removed, temp_mean = clean_data(raw)

    while True:  # Keep showing the menu until the user chooses Exit
        print("\n1. Summary\n2. Clean & Plot\n3. Rainfall Bar Chart\n4. Exit")
        choice = input("Menu option: ").strip()
        if choice == "1":
            show_summary(df)
        elif choice == "2":
            clean_and_plot(df, duplicates_removed, temp_mean)
        elif choice == "3":
            rainfall_bar_chart(df)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()  # Run the interactive program when this file is executed directly
