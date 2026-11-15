#Weather Data Analyser

import pandas as pd #this line imports the pandas library and gives it the alias pd, this is used to data analysis and manipulation, especially for working with tabular data like CSV files
import matplotlib.pyplot as plt #this line imports the pyplot module from the matplotlib library and gives it the alias plt, this is used for creating visualizations like line plots, bar charts, and scatter plots

columns = ["Date", "Temp", "Humidity", "Rainfall"] #this line defines a list of column names that will be used when loading the CSV file, these names correspond to the data in the CSV file

def load_data():
    """Asks for a file  name until a valid file is given, then loads it."""
    while True: #keep asking unitl the file is found
        file_name = input("Enter CSV file name: ").strip() #this line prompts the user to enter the name of a CSV file, and removes any leading or trailing whitespace from the input
        try: #try to open the file
            df = pd.read_csv(file_name, header=None, names=columns) #this line attempts to read the CSV file into a pandas DataFrame, using the specified column names and indicating that there is no header row in the file
            return df #if successful, return the DataFrame
        except FileNotFoundError: #this error happens if the file doesn't exist
            print(f"Error: File '{file_name}' not found. Please enter a valid file name.") #if the file is not found, print an error message and prompt the user again
def clean_data(df):
    """Removes duplicates and fills missing values. Returns clean table and counts."""
    df = df[df["Date"] != "Date"] #this line removes any rows where the "Date" column has the value "Date", which indicates that the row is a header row that was mistakenly included in the data
    for col in ["Temp", "Humidity", "Rainfall"]: #this loop iterates over the specified columns
        df[col] = pd.to_numeric(df[col], errors="coerce") #this line converts the values in each column to numeric types, replacing any non-numeric values with NaN (missing values)

    rows_before = len(df) #this line counts the number of rows in the DataFrame before removing duplicates
    df = df.drop_duplicates() #this line removes any duplicate rows from the DataFrame
    duplicates_removed = rows_before - len(df) #this line calculates the number of duplicate rows that were removed
    # Mean of Temp using NumPy (dropna() leaves out the missing values)
    temp_mean = np.mean(df["Temp"].dropna()) #this line calculates the mean (average) temperature, ignoring any missing values
    df["Temp"] = df["Temp"].fillna(temp_mean) #this line fills any missing temperature values with the calculated mean temperature
    humidity_mean = np.mean(df["Humidity"].dropna()) #this line calculates the mean (average) humidity, ignoring any missing values
    df["Humidity"] = df["Humidity"].fillna(humidity_mean) #this line fills any missing humidity values with the calculated mean humidity
    df["Rainfall"] = df["Rainfall"].fillna(0) #this

    df = df.reset_index(drop=True) #this line resets the index of the DataFrame, dropping the old index and creating a new one that starts from 0
    return df, duplicates_removed, temp_mean #this line returns the cleaned DataFrame, the number of duplicates removed, and the mean temperature

def show_summary(df):
    """Option 1: prints hottest/coldest day, average and total rainfall."""
    temps = df["Temp"].to_numpy() #this line converts the "Temp" column of the DataFrame to a NumPy array
    average = np.mean(temps) #this line calculates the average temperature
    max_temp = np.max(temps) #this line finds the maximum temperature
    min_temp = np.min(temps) #this line finds the minimum temperature
    std_dev = np.std(temps) #this line calculates the standard deviation of the temperatures

    if len(df) == 1: #this condition checks if there is only one row of data in the DataFrame
        print(f"Average Temp: {average:.2f} C | Max: {max_temp:g} | "
              f"Min: {min_temp:g} | Std Dev: {std_dev:.2f}") #if there is only one row, print the average, max, min, and standard deviation of the temperature
    else: #if there are multiple rows of data
        hottest_date = df["Date"].iloc[np.argmax(temps)] #this line finds the date corresponding to the maximum temperature
        coldest_date = df["Date"].iloc[np.argmin(temps)] #this line finds the date corresponding to the minimum temperature
        total_rain = np.sum(df["Rainfall"]) #this line calculates the total rainfall by summing the "Rainfall" column
        print(f"Average Temp: {average:.2f} C | Max: {max_temp:g} on {hottest_date} | "
              f"Min: {min_temp:g} on {coldest_date} | Std Dev: {std_dev:.2f} | Total Rainfall: {total_rain:.2f}") #print the average, max, min, standard deviation of the temperature, and total rainfall

        def clean_and_plot(df, duplicates_removed, temp_mean):
            """Option 2: shows the cleaned report and draws the line chart."""
            print(f"Duplicates removed: {duplicates_removed} / "
                  f"Missing Temp filled with mean: {temp_mean:.2f}") #this line prints the number of duplicates removed and the mean temperature used to fill missing values
            print(f"Cleaned rows: {len(df)} / Line chart 'Temperature Trend' displayed") #this line prints the number of cleaned rows and indicates that a line chart will be displayed
            plt.figure() #this line creates a new figure for the plot
            plt.plot(df["Date"], df["Temp"], marker='o') #this line plots the temperature trend over time
            plt.title("Temperature Trend") #this line sets the title of the plot
            plt.xlabel("Date") #this line sets the label for the x-axis
            plt.ylabel("Temperature (C)") #this line sets the label for the y-axis
            plt.xticks(rotation=30) #this line rotates the x-axis labels for better readability
            plt.tight_layout() #this line adjusts the layout of the plot to prevent overlap
            plt.show() #this line displays the plot

        def rainfall_bar_chart(df):
            """Option 3: draws a bar chart of rainfall."""
            plt.figure() #this line creates a new figure for the plot
            plt.bar(df["Date"], df["Rainfall"]) #this line creates a bar chart of rainfall over time
            plt.title("Rainfall Bar Chart") #this line sets the title of the plot
            plt.xlabel("Date") #this line sets the label for the x-axis
            plt.ylabel("Rainfall (mm)") #this line sets the label for the y-axis
            plt.xticks(rotation=30) #this line rotates the x-axis labels for better readability
            plt.tight_layout() #this line adjusts the layout of the plot to prevent overlap
            plt.show() #this line displays the plot

        def main():
            """Main program: load -> clean -> menu."""
            raw = load_data() #this line calls the load_data function to load the CSV file into a DataFrame
            print(f"Loaded {len(raw)} rows, columns: {', '.join(COLUMNS)}") #this line prints the number of rows loaded and the column names
            df, dups, temp_mean = clean_data(raw) #this line calls the clean_data function to clean the DataFrame and returns the cleaned DataFrame, number of duplicates removed, and mean temperature

            while True: #this loop continues until the user chooses to exit
                print("/n1. Summary/n2. Clean and Plot/n3. Rainfall Bar Chart/n4. Exit") #this line prints the menu options for the user
                choice = input("Menu option: ").strip() #this line prompts the user to enter a menu option and removes any leading or trailing whitespace
                if choice == "1": #if the user chooses option 1
                    show_summary(df) #this line calls the show_summary function to display the summary of the data
                elif choice == "2": #if the user chooses option 2
                    clean_and_plot(df, dups, temp_mean) #this line calls the clean_and_plot function to display the cleaning report and plot the temperature trend
                elif choice == "3": #if the user chooses option 3
                    rainfall_bar_chart(df) #this line calls the rainfall_bar_chart function to display the bar chart of rainfall   
                elif choice == "4": #if the user chooses option 4
                    print("goodbye!") #this line prints a goodbye message
                    break #this line breaks the loop and exits the program
                else: #if the user enters an invalid option
                    print("Invalid option. Please choose 1-4.") #this line prints an error message indicating that the user must choose a valid option

        main() #this line calls the main function to start the program

