#!/usr/bin/env python3

import pandas as pd  # type: ignore
import streamlit as st  # type: ignore
from classifiers import Knn
from data.data_process import DataProcess
from data.data_show import ShowData
from data.data_clean import CleanData
from plot.plot import Plot


player_stats = pd.read_csv('Player Shooting.csv')
injury_data = pd.read_csv(
    'NBA Player Injury Stats(1951 - 2023).csv')
team_data = pd.read_csv('Player Totals.csv')


def main():
    st.title("NBA Player injury Prediction")

    player_df: pd.DataFrame = DataProcess(
        player_stats, injury_data, team_data).merge_data()

    st.subheader("Dataset Preview")
    st.dataframe(player_df.head())

    st.subheader("Dataset Size")
    st.write(player_df.shape)

    # Displaying the data stats of the player_df
    ShowData.output_df(player_df)

    # Displaying missing values and categorical columns
    st.title("Missing Values & Categorical Columns Info")
    ShowData.show_cat_miss_data(player_df)

    st.title("Handle missing data")
    # Dropping columns with all missing values
    player_df = CleanData.drop_empty_columns(player_df)
    player_df = CleanData.drop_cols(
        player_df, ['birth_year_x', 'Acquired', 'Relinquished'])
    player_df = CleanData.fill_missing_with_column_average(player_df)

    # Extracting injury information from the 'Notes' column
    st.title("Extracting Injury Information from Notes and show final DataFrame")
    player_df = CleanData.extract_injury_info(player_df)
    st.write(player_df.head(50))
    ShowData.show_cat_miss_data(player_df)
    st.write(player_df.shape)

    # Plotting the data
    plotter = Plot(player_df)

    st.title("Injury Distribution Plot")
    plotter.plot_injury_distribution()  # Display the injury type distribution plot

    st.title("Injury Status Plot")
    plotter.plot_injury_status()  # Display the injury status plot

    st.title("Injury Status by Type Plot")
    plotter.plot_injury_by_type_and_status()  # Display injury status by type plot

    st.title("Injury Counts by Type")
    plotter.plot_injury_counts()  # Display injury counts by type plot


if __name__ == '__main__':
    main()
