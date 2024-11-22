import pandas as pd  # type:ignore
from dataclasses import dataclass

# Author: Wilkenson H
# Date: 2021-09-26


@dataclass
class DataProcess:
    """Data processing class to merge player_stats, injury_data, and team_data.

    Attributes:
    player_stats: pd.DataFrame
    injury_data: pd.DataFrame
    team_data: pd.DataFrame

    Methods: 
    merge_data: Merges player_stats, injury_data, and team_data on player_id and season.

    return: pd.DataFrame  

    """
    player_stats: pd.DataFrame
    injury_data: pd.DataFrame
    team_data: pd.DataFrame

    def merge_data(self):
        # Merge player_stats and injury_data on player_id
        merged_data = pd.merge(
            self.player_stats, self.team_data, on=['player_id', 'season'], how='left')

        # handle unbalanced data by taking the first n rows of injury_data
        merged_data = pd.concat(
            [merged_data, self.injury_data.head(len(merged_data))], axis=1)

        return merged_data

    # data stats

    def data_stats(self, data_df: pd.DataFrame):
        data_df = data_df.describe()
        data_df_shape = data_df.shape
        data_df_columns = data_df.columns
        data_df_index = data_df.index
        data_df_values = data_df.values
        data_df_info = data_df.info()
        data_df_head = data_df.head()
        data_df_tail = data_df.tail()
        data_df_dtypes = data_df.dtypes

        return data_df, data_df_shape, data_df_columns, data_df_index, data_df_values, data_df_info, data_df_head, data_df_tail, data_df_dtypes
