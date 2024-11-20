import pandas as pd

injury_df = pd.read_csv('NBA Player Injury Stats(1951 - 2023).csv')
players_df = pd.read_csv('Player Totals.csv')

#Issue, we need to merge on a column that is the same in both dataframes.
df = injury_df.merge(players_df, how='outer')
print(df)