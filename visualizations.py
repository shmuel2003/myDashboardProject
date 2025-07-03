import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, dataframe):
        self.df = dataframe

    def average_tip_by_day(self):
        avg = self.df.groupby("day")["tip"].mean().reset_index()
        fig = px.bar(avg, x='day', y='tip', title='Average Tip per Day')
        return fig

    def tip_vs_total_bill(self):
        fig, ax = plt.subplots()
        sns.scatterplot(data=self.df, x="total_bill", y="tip", hue="sex", ax=ax)
        ax.set_title("Scatter: Tip vs Total Bill")
        return fig

    def tip_distribution(self):
        fig = px.histogram(self.df, x="tip", nbins=20, title="Distribution of Tips")
        return fig