# ==========================================================
# PS 87 - Weather Data Analyzer
# Concepts: Pandas, NumPy, Matplotlib, Data Cleaning
# ==========================================================

import pandas as pd                  # Pandas: loads and cleans table (CSV) data
import numpy as np                   # NumPy: does the maths (mean, max, min, std)
import matplotlib.pyplot as plt      # Matplotlib: draws the charts

COLUMNS = ["Date", "Temp", "Humidity", "Rainfall"]   # The 4 column names of our CSV file


def load_data():
    """Asks for a file name until a valid file is given, then loads it."""
    while True:                                          # Keep asking until the file is found
        file_name = input("Enter CSV file name: ").strip()   # Read the file name typed by the user
        try:                                             # Try to open the file
            # header=None -> the file has no header row; names=COLUMNS -> we give the column names
            df = pd.read_csv(file_name, header=None, names=COLUMNS)
            return df                                    # File loaded, send the table back
        except FileNotFoundError:                        # This error happens if the file doesn't exist
            print(f"Error: File '{file_name}' not found. Please enter a valid file name.")


def clean_data(df):
    """Removes duplicates and fills missing values. Returns clean table and counts."""
    # If the file DID have a header row ("Date,Temp,..."), remove that row
    df = df[df["Date"] != "Date"]
    # Convert Temp, Humidity, Rainfall to numbers; bad/empty values become NaN (missing)
    for col in ["Temp", "Humidity", "Rainfall"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    rows_before = len(df)                                # Count rows before removing duplicates
    df = df.drop_duplicates()                            # Remove rows that are exact copies
    duplicates_removed = rows_before - len(df)           # How many duplicate rows were removed

    # Mean of Temp using NumPy (dropna() leaves out the missing values)
    temp_mean = np.mean(df["Temp"].dropna())
    df["Temp"] = df["Temp"].fillna(temp_mean)            # Fill missing Temp with that mean
    humidity_mean = np.mean(df["Humidity"].dropna())     # Mean of Humidity
    df["Humidity"] = df["Humidity"].fillna(humidity_mean)  # Fill missing Humidity with mean
    df["Rainfall"] = df["Rainfall"].fillna(0)            # Missing rainfall means no rain -> 0

    df = df.reset_index(drop=True)                       # Re-number rows 0,1,2... neatly
    return df, duplicates_removed, temp_mean             # Send back clean data and info


def show_summary(df):
    """Option 1: prints hottest/coldest day, average and total rainfall."""
    temps = df["Temp"].to_numpy()                        # Temp column as a NumPy array
    average = np.mean(temps)                             # Average temperature
    max_temp = np.max(temps)                             # Highest temperature
    min_temp = np.min(temps)                             # Lowest temperature
    std_dev = np.std(temps)                              # Standard deviation (how spread out)

    if len(df) == 1:                                     # Boundary case: only one row of data
        print(f"Average Temp: {average:.2f} C | Max: {max_temp:g} | "
              f"Min: {min_temp:g} | Std Dev: {std_dev:.2f}")
    else:                                                # Normal case: many rows
        hottest_date = df["Date"].iloc[np.argmax(temps)]   # Date of the hottest day
        coldest_date = df["Date"].iloc[np.argmin(temps)]   # Date of the coldest day
        total_rain = np.sum(df["Rainfall"].to_numpy())     # Total rainfall
        print(f"Average Temp: {average:.2f} C | Max: {max_temp:g} ({hottest_date}) | "
              f"Min: {min_temp:g} ({coldest_date}) | Total Rainfall: {total_rain:g} mm")


def clean_and_plot(df, duplicates_removed, temp_mean):
    """Option 2: shows the cleaning report and draws the line chart."""
    print(f"Duplicates removed: {duplicates_removed} | "
          f"Missing Temp filled with mean: {temp_mean:.2f}")
    print(f"Cleaned rows: {len(df)} | Line chart 'Temperature Trend' displayed")
    plt.figure()                                         # Start a new empty chart
    plt.plot(df["Date"], df["Temp"], marker="o")         # Line chart: Date vs Temp
    plt.title("Temperature Trend")                       # Chart title
    plt.xlabel("Date")                                   # Label for the x-axis
    plt.ylabel("Temperature (C)")                        # Label for the y-axis
    plt.xticks(rotation=30)                              # Tilt dates so they don't overlap
    plt.tight_layout()                                   # Fit everything inside the window
    plt.show()                                           # Display the chart


def rainfall_bar_chart(df):
    """Option 3: draws the bar chart of rainfall."""
    plt.figure()                                         # Start a new empty chart
    plt.bar(df["Date"], df["Rainfall"])                  # Bar chart: Date vs Rainfall
    plt.title("Daily Rainfall")                          # Chart title
    plt.xlabel("Date")                                   # Label for the x-axis
    plt.ylabel("Rainfall (mm)")                          # Label for the y-axis
    plt.xticks(rotation=30)                              # Tilt dates
    plt.tight_layout()                                   # Fit everything inside the window
    plt.show()                                           # Display the chart


def main():
    """Main program: load -> clean -> menu."""
    raw = load_data()                                    # Step 1: load the CSV file
    print(f"Loaded {len(raw)} rows, columns: {', '.join(COLUMNS)}")  # Short data summary
    df, dups, temp_mean = clean_data(raw)                # Step 2: clean the data

    while True:                                          # Show the menu again and again
        print("\n1. Summary\n2. Clean & Plot\n3. Rainfall Bar Chart\n4. Exit")
        choice = input("Menu option: ").strip()          # Read the user's choice
        if choice == "1":
            show_summary(df)                             # Show the statistics
        elif choice == "2":
            clean_and_plot(df, dups, temp_mean)          # Show cleaning report + line chart
        elif choice == "3":
            rainfall_bar_chart(df)                       # Show bar chart
        elif choice == "4":
            print("Goodbye!")                            # Say bye
            break                                        # Stop the loop -> program ends
        else:
            print("Invalid option. Please choose 1-4.")  # Wrong input message


main()                                                   # Start the program