
import pandas as pd  # type: ignore
from dataclasses import dataclass
import streamlit as st  # type: ignore

"""
Author: Wilkenson H. 
"""


@dataclass
class ShowData:
    @staticmethod
    def data_stats(data_df: pd.DataFrame):
        data_df = data_df.describe()
        data_df_columns = data_df.columns
        data_df_index = data_df.index
        data_df_values = data_df.values
        data_df_info = data_df.info()
        data_df_head = data_df.head()
        data_df_tail = data_df.tail()
        data_df_dtypes = data_df.dtypes

        output = {
            'data_df_description': data_df,
            'data_df_columns': data_df_columns,
            'data_df_index': data_df_index,
            'data_df_values': data_df_values,
            'data_df_info': data_df_info,
            'data_df_head': data_df_head,
            'data_df_tail': data_df_tail,
            'data_df_dtypes': data_df_dtypes
        }

        return output

    @staticmethod
    def output_df(player_df: pd.DataFrame):
        stats = ShowData.data_stats(player_df)

        # Displaying each info part in its own table
        st.subheader("Description")
        st.dataframe(stats['data_df_description'])  # Display describe() result

        st.subheader("Columns")
        st.write(stats['data_df_columns'])  # Display columns as a list

        st.subheader("Index")
        st.write(stats['data_df_index'])  # Display index as a list

        st.subheader("Columns and Index")

        st.subheader("Values (First 5 rows)")
        st.write(stats['data_df_values'])  # Display values

        st.subheader("Head (First 5 Rows)")
        # Display first 5 rows of the DataFrame
        st.dataframe(stats['data_df_head'])

        st.subheader("Tail (Last 5 Rows)")
        # Display last 5 rows of the DataFrame
        st.dataframe(stats['data_df_tail'])

        st.subheader("Data Types of Columns")
        st.write(stats['data_df_dtypes'])  # Display data types of each column

    @staticmethod
    def missing_and_categorical_stats(data_df: pd.DataFrame):
        # Checking for missing values
        missing_values = data_df.isnull().sum()

        # Identifying categorical columns and their unique counts
        categorical_columns = data_df.select_dtypes(include=['object']).columns
        categorical_unique_counts = {
            col: data_df[col].nunique() for col in categorical_columns}

        # Identifying numeric columns
        numeric_columns = data_df.select_dtypes(include=['number']).columns

        # Return a dictionary with missing and categorical stats
        return {
            'missing_values': missing_values,
            'categorical_columns': categorical_columns,
            'categorical_unique_counts': categorical_unique_counts,
            'numeric_columns': numeric_columns
        }

    @staticmethod
    def show_cat_miss_data(player_df: pd.DataFrame):
        # Missing and Categorical Stats
        st.subheader("Missing Values & Categorical Columns Info")
        missing_and_categorical_stats = ShowData.missing_and_categorical_stats(
            player_df)

        # Display Categorical Columns and their unique counts
        st.write("Categorical Columns and Unique Value Counts:")
        st.write(missing_and_categorical_stats['categorical_unique_counts'])

        # Display Numeric Columns
        st.write("Numeric Columns:")
        st.write(missing_and_categorical_stats['numeric_columns'])

        # Display Missing Values
        st.write("Missing Values Per Column:")
        st.dataframe(missing_and_categorical_stats['missing_values'])
