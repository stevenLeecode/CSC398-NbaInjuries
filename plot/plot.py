import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass
import streamlit as st

"""
Author: Wilkenson H. 
"""


@dataclass
class Plot:
    data_df: pd.DataFrame

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
        st.pyplot(plt)
