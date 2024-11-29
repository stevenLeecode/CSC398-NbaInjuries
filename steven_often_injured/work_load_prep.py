import pandas as pd

original_df = pd.read_csv("final_player_data.csv")
'''
Columns for workload:

Ignore the x, means both are the same values in between
the two datasets Player Shooting.csv and Player totals.csv

mp_x = Minutes Played
orb = offensive rebounds
drb = defensive rebounds
pf = personal fouls
fga = field goal attempts
stl = steals
blk = blocks
pts = points
age_x = age
x2pa = 2 point attempts
x3pa = 3 point attempts
experience_y = years of experience (at their current season)

Example: Stephen Curry

'''

work_load = original_df[['season','mp_x', 'fga', 'fta','orb','drb', 'ast', 'stl', 'blk', 'pf', 'pts', 'age_x', 'x2pa', 'x3pa', 'experience_y']]
#Drop all rows greater than 2018 season
work_load.drop(work_load[work_load['season'] > 2018].index, axis=0, inplace=True)
#Group each column by season and sum each column.
work_load = work_load.groupby('season').sum()
#The lowest season in the original datset is 1997, so can't do anything below that.
#print(original_df['season'].min())