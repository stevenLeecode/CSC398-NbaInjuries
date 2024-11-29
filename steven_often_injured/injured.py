import pandas as pd

#Nba PLayer Injury Stats has dates up to 2023, but final_player_data.csv goes up to 2018.
#From 2019-2023, I think the rows got dropped?

original_df = pd.read_csv("final_player_data.csv")
df = original_df[['Injured', 'Date']]

#Example of Date: 1951-09-16
#Parsing the data to extract only the year.
df['Year'] = df['Date'].str.split('-').str[0]
df.drop('Date', inplace=True, axis=1)

#Include only the players that are injured.
df.drop(df[df['Injured'] == 0].index, inplace=True)
#print(df['Injured'].value_counts())
#Filter out years before 1997 for other dataset.
df['Year'] = df['Year'].astype(int)
df = df.loc[df['Year'] >= 1997]

injured_count = df.value_counts().reset_index()
injured_count.drop("Injured", inplace=True, axis=1)
injured_count.rename(columns={"count":"injuries"}, inplace=True)
injured_count = injured_count.sort_values('Year', ascending=False)
injured_count.rename(columns={"Year":"season"}, inplace=True)
