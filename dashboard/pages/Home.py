import streamlit as st
from utils import load_data

df = load_data()

st.title("🏠 Dashboard Overview")

st.markdown("### Customer Churn Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", len(df))

with col2:
    churn_rate = (df["Churn"] == "Yes").mean() * 100
    st.metric("Churn Rate", f"{churn_rate:.1f}%")

with col3:
    st.metric("Average Tenure", f"{df['tenure'].mean():.1f} Months")

with col4:
    st.metric("Average Monthly Charge", f"${df['MonthlyCharges'].mean():.2f}")

st.divider()

st.subheader("Dataset Preview")

st.dataframe(df.head(), use_container_width=True)

st.divider()

st.subheader("Project Objective")

st.write("""
The objective of this project is to analyze customer behavior,
identify the factors contributing to customer churn,
and build a machine learning model capable of predicting whether a customer is likely to cancel their subscription.
""")