import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/stevenLeecode/CSC398-NbaInjuries/refs/heads/main/final_player_data.csv')

#Total injuries for each part of the season

#month = df['Date'].str.split('-', expand=True)[1]
#day = df['Date'].str.split('-', expand=True)[2]
df['Date'] = pd.to_datetime(df['Date'])
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df = df.loc[df['Injured'] == 1] #Select all the injuries

injury_keywords = ['placed', 'torn', 'side muscle', 'illness', 'broken', 'sprain', 'knee', 'ankle', 'muscle', 'back', 'sore', 'surgery', 'hip',
                           'toe', 'leg', 'elbow', 'abdominal', 'quad', 'hand', 'finger', 'thigh', 'neck', 'arm', 'rib', 'knee', 'hamstring', 'achilles',
                           'foot', 'wrist', 'shoulder', 'head', 'concussion', 'groin', 'calf',
                           'hamstring', 'achilles', 'foot', 'wrist', 'shoulder', 'head', 'concussion', 'groin', 'calf']

#Return all where value_counts is true

for i in injury_keywords:
  df[i] = df['Notes'].str.contains(i)

#Create new dataframe
injury_type = df['Notes'].str.contains('placed').value_counts().reset_index()

#Append values to dataframe to count each injury
for i in injury_keywords:
  injury_type[i] = df['Notes'].str.contains(i).value_counts()


injury_type.drop("placed", axis=1, inplace=True)
injury_type.drop("count", axis=1, inplace=True)
#Achilles is NAN so drop column
injury_type.isna().sum()
injury_type.drop("achilles", axis=1, inplace=True)
#drop True row
total_injury_type = injury_type[injury_type['Notes'] == False]
#drop Notes and Placed columns(Will represent the values of false)
total_injury_type = total_injury_type.drop("Notes", axis=1)

top_injuries = total_injury_type.max().sort_values(ascending=False)
top_10_injuries = top_injuries.head(10)

#Plot top 10 injuries

fig, ax = plt.subplots(figsize=(10, 6))
colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'black', 'yellow', 'grey', 'violet']
bars = ax.bar(top_10_injuries.index, top_10_injuries.values, color=colors)

# Add labels on top of bars
ax.bar_label(bars)
ax.set_xlabel("Injury Type")
ax.set_ylabel("Injuries")
ax.set_title("Top 10 injuries (1951 - 2023)")
plt.show()