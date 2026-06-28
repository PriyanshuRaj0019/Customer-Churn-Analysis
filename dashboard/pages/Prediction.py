import streamlit as st
import pandas as pd
from utils import load_model

st.set_page_config(layout="wide")

st.title("🤖 Customer Churn Prediction")

st.write("Enter customer details to predict whether the customer is likely to churn.")

model = load_model()

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox("Gender", ["Male", "Female"])

    senior = st.selectbox("Senior Citizen", [0, 1])

    partner = st.selectbox("Partner", ["Yes", "No"])

    dependents = st.selectbox("Dependents", ["Yes", "No"])

    tenure = st.slider("Tenure (Months)", 0, 72, 24)

    phone = st.selectbox("Phone Service", ["Yes", "No"])

    multiple = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

with col2:

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

    device = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly = st.number_input(
        "Monthly Charges",
        min_value=18.0,
        max_value=120.0,
        value=70.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=18.0,
        value=1500.0
    )

if st.button("Predict Churn", use_container_width=True):

    customer = pd.DataFrame({
        "gender":[gender],
        "SeniorCitizen":[senior],
        "Partner":[partner],
        "Dependents":[dependents],
        "tenure":[tenure],
        "PhoneService":[phone],
        "MultipleLines":[multiple],
        "InternetService":[internet],
        "OnlineSecurity":[online_security],
        "OnlineBackup":[online_backup],
        "DeviceProtection":[device],
        "TechSupport":[tech],
        "StreamingTV":[tv],
        "StreamingMovies":[movies],
        "Contract":[contract],
        "PaperlessBilling":[paperless],
        "PaymentMethod":[payment],
        "MonthlyCharges":[monthly],
        "TotalCharges":[total]
    })

    prediction = model.predict(customer)[0]

    probability = model.predict_proba(customer)[0][1]

    st.divider()

    if prediction == 1:
        st.error("⚠️ High Risk of Churn")
    else:
        st.success("✅ Customer is Likely to Stay")

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    st.progress(float(probability))

    st.subheader("Suggested Business Action")

    if probability >= 0.7:
        st.write("""
- Contact customer immediately
- Offer retention discount
- Recommend long-term contract
- Assign customer support representative
""")

    elif probability >= 0.4:
        st.write("""
- Send promotional offers
- Recommend value-added services
- Monitor engagement
""")

    else:
        st.write("""
- Customer is relatively stable
- Continue regular engagement
""")