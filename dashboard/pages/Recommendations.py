import streamlit as st

st.set_page_config(layout="wide")

st.title("💡 Business Recommendations")

st.write(
    "Recommendations derived from the exploratory data analysis and machine learning model."
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("Key Findings")

    st.success("""
✔ Customers with month-to-month contracts churn the most.
""")

    st.success("""
✔ Customers with shorter tenure are more likely to leave.
""")

    st.success("""
✔ Higher monthly charges increase churn probability.
""")

    st.success("""
✔ Customers without Tech Support have higher churn.
""")

    st.success("""
✔ Electronic Check customers show the highest churn.
""")

with col2:

    st.subheader("Business Recommendations")

    st.info("""
**1. Promote Long-Term Contracts**

Offer discounts for annual subscriptions to improve retention.
""")

    st.info("""
**2. Improve Technical Support**

Provide proactive technical assistance to reduce dissatisfaction.
""")

    st.info("""
**3. Reward Loyal Customers**

Introduce loyalty rewards for long-tenure customers.
""")

    st.info("""
**4. Target High-Risk Customers**

Identify customers with high churn probability and launch personalized retention campaigns.
""")

    st.info("""
**5. Optimize Pricing**

Review pricing strategies for customers with high monthly charges.
""")

st.divider()

st.subheader("Conclusion")

st.write("""
The analysis indicates that customer churn is primarily influenced by contract type, tenure, monthly charges, payment method, and technical support availability.

By focusing on these factors, businesses can improve customer satisfaction, reduce churn, and increase long-term revenue.
""")