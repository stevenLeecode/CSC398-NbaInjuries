#Steven

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

'''
NBA REGULAR SEASON : OCTOBER -> APRIL
First NBA games are usually at the end of October.

Beginning of season = October - December
Middle of season = January - February
End of season = March - April

'''
october = df.loc[(df['month'] == 10) & (df['day'] >= 20)]
october = october['Injured'].count() #Last 10 days of october 

beginning_of_season = df.loc[(df['month'] > 10)] # November and December.
middle_of_season = df.loc[df['month'] <= 2] #January and February
end_of_season = df.loc[(df['month'] <= 4) & (df['month'] > 3)] #March and April

#print("October: ", october['Injured'].count())
print("Beginning of season injuries: ", beginning_of_season['Injured'].count() + october)
print("Middle of season injuries: ", middle_of_season['Injured'].count())
print("End of season injuries: ", end_of_season['Injured'].count())

data = {
    'October-December': beginning_of_season['Injured'].count() + october,
    'January-February': middle_of_season['Injured'].count(),
    'March-April': end_of_season['Injured'].count()
}

seasonal_injuries = pd.Series(data)
#seasonal_injuries.columns = ['season_type', 'injuries']
print(seasonal_injuries)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(seasonal_injuries.index, seasonal_injuries.values, color=['red', 'green', 'blue'])

# Add labels on top of bars
ax.bar_label(bars)
ax.set_xlabel("Time-Frame")
ax.set_ylabel("Injuries")
ax.set_title("Total injuries for each part of season (1951-2023)")
plt.show()