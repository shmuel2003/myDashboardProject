import streamlit as st
from data_loader import DataLoader
from visualizations import Visualizer

# Title
st.title("Modular Streamlit Dashboard")

# Load data
@st.cache_data
def get_data():
    loader = DataLoader()
    return loader.load_data()

df = get_data()
st.subheader("Data Preview")
st.dataframe(df.head())

# Initialize visualizer
viz = Visualizer(df)

# Visualization 1
st.subheader("Average Tip by Day")
st.plotly_chart(viz.average_tip_by_day())

# Visualization 2
st.subheader("Tip vs Total Bill")
st.pyplot(viz.tip_vs_total_bill())

# Visualization 3
st.subheader("Tip Distribution")
st.plotly_chart(viz.tip_distribution())

# Optional sidebar filter
st.sidebar.header("Filters")
selected_day = st.sidebar.selectbox("Select a day", df["day"].unique())
filtered_df = df[df["day"] == selected_day]
st.subheader(f"Data for {selected_day}")
st.dataframe(filtered_df)