import streamlit as st
import pandas as pd

# Function to load CSV file
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df, None
    except Exception as e:
        return None, str(e)

# Function to calculate missing values and DQI
def calculate_dqi(df):
    total_values = df.size
    if total_values == 0:
        return 0.0, 0
    missing_values = df.isnull().sum().sum()
    dqi = (1 - (missing_values / total_values)) * 100
    return dqi, missing_values

# Streamlit app starts here
st.title("📊 Data Quality Dashboard")

# Input for CSV file path
file_path = st.text_input(
    "Enter CSV file path:",
    "/workspaces/AI_DATA_ANALYSIS_/src/Module 8/Data Quality Scoring & Reporting/students.csv"
)

if file_path:
    df, error = load_data(file_path)
    if error:
        st.error(f"Failed to load file: {error}")
    else:
        st.success("File loaded successfully!")
        st.write("### Data Preview")
        st.dataframe(df.head())

        # Calculate and show DQI and missing values
        dqi, missing_values = calculate_dqi(df)
        st.metric(label="Data Quality Index (DQI)", value=f"{dqi:.2f}%")
        st.metric(label="Total Missing Values", value=missing_values)

        # Show missing values by column as a bar chart
        st.write("### Missing Values by Column")
        missing_per_column = df.isnull().sum()
        st.bar_chart(missing_per_column)
