import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:/Users/Kasbe/Downloads/csc398proj/CSC398-NbaInjuries/NBA Player Injury Stats(1951 - 2023).csv"
injuries = pd.read_csv(file_path)

# Convert 'Date' column to datetime format and drop invalid dates
injuries['Date'] = pd.to_datetime(injuries['Date'], errors='coerce')
injuries = injuries[injuries['Date'].notnull()]

# Categorize season periods
def categorize_season(month):
    if month in [10, 11, 12]:
        return 'Beginning'
    elif month in [1, 2]:
        return 'Middle'
    elif month in [3, 4]:
        return 'End'
    else:
        return 'Off-Season'

# Apply categorization
injuries['Month'] = injuries['Date'].dt.month
injuries['SeasonPeriod'] = injuries['Month'].apply(categorize_season)
injuries = injuries.loc[injuries['Injured'] == 1] #Select all the injuries

# Count injuries by season period
season_counts = injuries['SeasonPeriod'].value_counts()
print("Injuries by Season Period:")
print(season_counts)

# Visualize the results
season_counts.plot(kind='bar', color='skyblue')
plt.title('Injuries by Season Period')
plt.xlabel('Season Period')
plt.ylabel('Number of Injuries')
plt.xticks(rotation=0)
plt.show()
