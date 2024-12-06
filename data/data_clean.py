from dataclasses import dataclass
import pandas as pd  # type: ignore

"""
Author: Wilkenson H. 
"""

@dataclass
class CleanData:

    @staticmethod
    def drop_empty_columns(data_df):
        """Drop columns that are completely empty (all NaN)."""
        data_df.dropna(axis=1, how='all', inplace=True)
        return data_df

    def drop_cols(data_df: pd.DataFrame, cols: list):
        """Drop columns that are completely empty (all NaN)."""

        data_df.drop(cols, axis=1, inplace=True)
        return data_df

    @staticmethod
    def fill_missing_with_column_average(data_df):
        """Fill missing numeric values in each column with the column's average."""
        numeric_cols = data_df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            # Calculate mean excluding NaN
            col_mean = data_df[col].mean(skipna=True)
            # Replace NaN with column mean
            data_df[col].fillna(col_mean, inplace=True)
        return data_df

    @staticmethod
    def drop_rows_with_missing_in_columns(data_df: pd.DataFrame, cols: list):
        """
        Drop rows where any of the specified columns contain NaN or None.

        Args:
            data_df (pd.DataFrame): The input DataFrame.
            cols (list): List of column names to check for missing values.

        Returns:
            pd.DataFrame: DataFrame with rows containing missing values in specified columns removed.
        """
        return data_df.dropna(subset=cols)

    @staticmethod
    def extract_injury_info(data_df: pd.DataFrame, notes_col: str = 'Notes', output_file: str = 'final_player_data.csv'):
        """
        Create 'Injury_type' and 'Injured' columns based on keywords in the 'Notes' column.

        Args:
            data_df (pd.DataFrame): The input DataFrame.
            notes_col (str): The column containing injury information (default is 'Notes').

        Returns:
            pd.DataFrame: The DataFrame with 'Injury_type' and 'Injured' columns added.
        """
        # Check if the notes column exists in the DataFrame
        if notes_col not in data_df.columns:
            raise KeyError(f"Column '{notes_col}' not found in the DataFrame.")

        # Define a list of injury-related keywords
        injury_keywords = ['placed', 'torn', 'side muscle', 'illness', 'broken', 'sprain', 'knee', 'ankle', 'muscle', 'back', 'sore', 'surgery', 'hip',
                           'toe', 'leg', 'elbow', 'abdominal', 'quad', 'hand', 'finger', 'thigh', 'neck', 'arm', 'rib', 'knee', 'hamstring', 'achilles',
                           'foot', 'wrist', 'shoulder', 'head', 'concussion', 'groin', 'calf'
                           'hamstring', 'achilles', 'foot', 'wrist', 'shoulder', 'head', 'concussion', 'groin', 'calf']

        # determine injury type and injured status
        def extract_injury(note):
            injury_found = False
            injury_type = None
            for keyword in injury_keywords:
                if isinstance(note, str) and keyword.lower() in note.lower():
                    injury_found = True
                    injury_type = keyword  # Capture the first match as the injury type
                    break  # No need to check further keywords
            return injury_type, 1 if injury_found else 0

        injury_info = data_df[notes_col].apply(
            lambda note: pd.Series(extract_injury(note)))

        # Assign the extracted injury information to the original DataFrame
        data_df[['Injury_type', 'Injured']] = injury_info

        data_df['Injury_type'].fillna('No injury', inplace=True)
        data_df.to_csv(output_file, index=False)
        return data_df
