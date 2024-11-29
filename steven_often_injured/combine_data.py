import pandas as pd
import injured
import work_load_prep

#Import dataframes
work_load = work_load_prep.work_load
injured = injured.injured_count

#merge dataframes to final data combination
combined = pd.merge(work_load, injured, on='season', how='outer')
#print(combined)
combined.to_csv('total_injuries.csv')