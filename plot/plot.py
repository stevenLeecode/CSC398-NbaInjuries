import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass
import streamlit as st


@dataclass
class Plot:
    data_df: pd.DataFrame

    def plot_injury_distribution(self):
        """
        Plot the distribution of injury types and the count of injured vs non-injured players.
        """
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.data_df, x='Injury_type',
                      order=self.data_df['Injury_type'].value_counts().index)
        plt.title('Injury Type Distribution')
        plt.xlabel('Injury Type')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        st.pyplot(plt)  # Use Streamlit's method to display the plot

    def plot_injury_status(self):
        """
        Plot the count of injured vs non-injured players.
        """
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.data_df, x='Injured')
        plt.title('Injury Status (Injured vs Non-Injured)')
        plt.xlabel('Injured (1) / Non-Injured (0)')
        plt.ylabel('Count')
        plt.xticks([0, 1], ['Non-Injured', 'Injured'])
        plt.tight_layout()
        st.pyplot(plt)  # Use Streamlit's method to display the plot

    def plot_injury_by_type_and_status(self):
        """
        Plot the injury status (Injured vs Non-Injured) by injury type.
        """
        plt.figure(figsize=(12, 7))
        sns.countplot(data=self.data_df, x='Injury_type', hue='Injured',
                      order=self.data_df['Injury_type'].value_counts().index)
        plt.title('Injury Status by Injury Type')
        plt.xlabel('Injury Type')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        st.pyplot(plt)  # Use Streamlit's method to display the plot

    def plot_injury_counts(self):
        """
        Plot the counts of injuries by type, separating injured and non-injured.
        """
        injury_counts = self.data_df.groupby(
            ['Injury_type', 'Injured']).size().unstack().fillna(0)
        injury_counts = injury_counts.sort_values(by=1, ascending=False)

        injury_counts.plot(kind='bar', stacked=False, figsize=(
            12, 6), color=['#66b3ff', '#ff6666'])
        plt.title('Injury Counts by Injury Type')
        plt.xlabel('Injury Type')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        st.pyplot(plt)  # Use Streamlit's method to display the plot
