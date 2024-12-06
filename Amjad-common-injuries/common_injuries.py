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

# Validate Season Period Categorization
season_validation = injuries.groupby('SeasonPeriod')['Month'].apply(lambda x: x.unique())
print("Validation of Season Period Categorization:")
print(season_validation)

# Count injuries by season period
season_counts = injuries['SeasonPeriod'].value_counts()
print("\nInjuries by Season Period:")
print(season_counts)

# Visualize injuries by season period
season_counts.plot(kind='bar', color='skyblue')
plt.title('Injuries by Season Period')
plt.xlabel('Season Period')
plt.ylabel('Number of Injuries')
plt.xticks(rotation=0)
plt.show()

# Analyze injuries over time (yearly trends)
injuries['Year'] = injuries['Date'].dt.year
yearly_counts = injuries['Year'].value_counts().sort_index()

# Visualize yearly trends
yearly_counts.plot(kind='line', figsize=(10, 6), color='green')
plt.title('Number of Injuries Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Injuries')
plt.grid(True)
plt.show()

# Analyze injuries by team
team_counts = injuries['Team'].value_counts()

# Check if there are any unexpected values in the 'Team' column
invalid_teams = injuries['Team'].isnull().sum()
print(f"\nNumber of entries with missing 'Team': {invalid_teams}")

# Visualize top 10 teams with the most injuries
team_counts.head(10).plot(kind='bar', color='orange', figsize=(10, 6))
plt.title('Top 10 Teams with Most Injuries')
plt.xlabel('Team')
plt.ylabel('Number of Injuries')
plt.xticks(rotation=45)
plt.show()

# Analyze common injury notes
notes_counts = injuries['Notes'].value_counts().head(10)

# Check for unexpected or null values in 'Notes'
invalid_notes = injuries['Notes'].isnull().sum()
print(f"Number of entries with missing 'Notes': {invalid_notes}")

# Visualize common notes
notes_counts.plot(kind='bar', color='purple', figsize=(10, 6))
plt.title('Most Common Injury Notes')
plt.xlabel('Reason/Note')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# Calculate accuracy of categorizations
total_entries = len(injuries)
valid_entries = total_entries - (invalid_teams + invalid_notes)
accuracy = (valid_entries / total_entries) * 100

# Summary report
print("\nSummary Report:")
print(f"Total Injuries: {total_entries}")
print(f"Valid Entries (with valid 'Team' and 'Notes'): {valid_entries}")
print(f"Categorization Accuracy: {accuracy:.2f}%")
print(f"Most Common Season Period: {season_counts.idxmax()}")
print(f"Team with Most Injuries: {team_counts.idxmax()}")
print(f"Most Frequent Injury Note: {notes_counts.idxmax()}")