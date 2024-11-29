import pandas as pd

df = pd.read_csv('NBA-Stats Dataset\Player Career Info.csv')
players = df.loc[:, ['player', 'num_seasons']]

print(players.loc[players['player'] == 'Bill Walton'])