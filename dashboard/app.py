import streamlit as st

st.set_page_config(
    page_title="Customer Churn Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Customer Churn Analysis Dashboard")

st.markdown("""
### Internship Project

This dashboard analyzes customer subscription data to identify churn patterns and predict whether a customer is likely to cancel their subscription.

### Features

- Customer Overview
- Exploratory Data Analysis
- Customer Churn Prediction
- Business Recommendations

Use the sidebar to navigate between pages.
""")

st.info("Select a page from the left sidebar.")