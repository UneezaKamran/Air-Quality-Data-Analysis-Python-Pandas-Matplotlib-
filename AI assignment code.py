import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Task 1
#1
df = pd.read_csv(r"C:/Users/uneez/AppData/Local/Temp/AweZip/Temp1/AweZip3/air+quality/AirQualityUCI.csv", sep=";", encoding="latin1")
#2Display First 10 rows
print("First 10 rows:")
print(df.head(10))
#3 Get dataset dimensions
print("Dataset Dimensions:")
print(df.shape)
#4 Displaying column names and datatype
print("Column names and Data types:")
print(df.dtypes)
#5 Checking for missing values
print("Missing values:")
print(df.isnull().sum())

# Task 2: Data Cleaning and Preparation
# Convert Date and Time into a single datetime column
df["Datetime"] = pd.to_datetime(df["Date"].astype(str) + " " + df["Time"].astype(str), 
                                format="%d/%m/%Y %H.%M.%S", errors='coerce')
# Set Datetime as the index
df = df.set_index("Datetime")
# Remove unnecessary columns if not needed (e.g., NMHC(GT))
df = df.drop(columns=["NMHC(GT)"], errors='ignore')
print(df)
# Handle missing values by filling with the mean of respective columns
df = df.apply(pd.to_numeric, errors='coerce') 
df = df.fillna(df.mean())
print(df)

# Task 3: Time-Series Analysis
# Resample data to calculate daily averages
daily_avg = df.resample('D').mean()
# Plot daily average levels
plt.figure(figsize=(12, 5))
daily_avg[['CO(GT)', 'NO2(GT)', 'PT08.S5(O3)']].plot()
plt.title("Daily Average Pollutant Levels")
plt.xlabel("Date")
plt.ylabel("Concentration")
plt.savefig(r"C:\Users\uneez\Documents\TASK1.pdf")
plt.legend(["CO", "NO2", "O3"])
plt.show()
# Find days with highest CO and NO2 levels
highest_co_day = daily_avg['CO(GT)'].idxmax()
highest_no2_day = daily_avg['NO2(GT)'].idxmax()
print(f"Highest CO level recorded on: {highest_co_day}")
print(f"Highest NO2 level recorded on: {highest_no2_day}")

# Task 4: Data Visualization
# Histogram for CO levels
df['CO(GT)'].hist(bins=30, edgecolor='black')
plt.title("Histogram of CO Levels")
plt.xlabel("CO Concentration")
plt.ylabel("Frequency")
plt.savefig(r"C:\Users\uneez\Documents\TASK3.pdf")
plt.show()
# Scatter plot for NO2 vs O3
sns.scatterplot(x=df['NO2(GT)'], y=df['PT08.S5(O3)'])
plt.title("Scatter Plot of NO2 vs O3")
plt.xlabel("NO2 Levels")
plt.ylabel("O3 Levels")
plt.savefig(r"C:\Users\uneez\Documents\TASK4.pdf")
plt.show()
# Box plot for O3 levels by month
df['Month'] = df.index.month
sns.boxplot(x=df['Month'], y=df['PT08.S5(O3)'])
plt.title("Box Plot of O3 Levels by Month")
plt.xlabel("Month")
plt.ylabel("O3 Levels")
plt.savefig(r"C:\Users\uneez\Documents\TASK5.pdf")
plt.show()
# Heatmap of correlations
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig(r"C:\Users\uneez\Documents\TASK6.pdf")
plt.show()

# Task 5: Advanced Analysis
# Rolling average (7-day) for CO levels
df['CO(GT)'].rolling(window=7).mean().plot(figsize=(12, 5))
plt.title("7-Day Rolling Average of CO Levels")
plt.xlabel("Date")
plt.ylabel("CO Levels")
plt.savefig(r"C:\Users\uneez\Documents\TASK7.pdf")
plt.show()
# Group by hour and calculate average levels
hourly_avg = df.groupby(df.index.hour).mean()
hourly_avg[['CO(GT)', 'NO2(GT)', 'PT08.S5(O3)']].plot()
plt.title("Average Pollutant Levels by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Concentration")
plt.legend(["CO", "NO2", "O3"])
plt.savefig(r"C:\Users\uneez\Documents\TASK8.pdf")
plt.show()
# Identify seasonal trends in pollutant levels
seasonal_avg = df.resample('M').mean()
plt.figure(figsize=(12, 5))
seasonal_avg[['CO(GT)', 'NO2(GT)', 'PT08.S5(O3)']].plot()
plt.title("Monthly Average Pollutant Levels (Seasonal Trends)")
plt.xlabel("Month")
plt.ylabel("Concentration")
plt.legend(["CO", "NO2", "O3"])
plt.savefig(r"C:\Users\uneez\Documents\TASK9.pdf")
plt.show()


