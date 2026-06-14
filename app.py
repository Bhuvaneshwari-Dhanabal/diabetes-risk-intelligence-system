import streamlit as st
import pandas as pd
import uuid
import os
from datetime import datetime

from src.diabetes_prediction import predict_diabetes
from src.risk_scoring import calculate_risk_score
from src.recommendation_engine import generate_recommendation
from src.anomaly_alerts import generate_alerts
from src.pdf_report import generate_pdf

os.makedirs("reports", exist_ok=True)

st.set_page_config(
    page_title="Patient Risk Intelligence System",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Diabetes Risk Intelligence System")
st.markdown(
    "### AI-Powered Diabetes Risk Assessment & Medical Report Generator"
)

st.divider()

st.header("🩺 Patient Information")

with st.form("patient_form"):

    patient_name = st.text_input(
        "Patient Name",
        placeholder="Enter patient name"
    )

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=30
        )

        glucose = st.number_input(
            "Glucose",
            min_value=0,
            max_value=300,
            value=120
        )

        bmi = st.number_input(
            "BMI",
            min_value=0.0,
            max_value=100.0,
            value=25.0
        )

        pregnancies = st.number_input(
            "Pregnancies",
            min_value=0,
            max_value=20,
            value=1
        )

    with col2:

        blood_pressure = st.number_input(
            "Blood Pressure",
            min_value=0,
            max_value=200,
            value=70
        )

        insulin = st.number_input(
            "Insulin",
            min_value=0,
            max_value=1000,
            value=80
        )

        skin_thickness = st.number_input(
            "Skin Thickness",
            min_value=0,
            max_value=100,
            value=20
        )

    submitted = st.form_submit_button(
        "🔍 Generate Medical Report"
    )

if submitted:

    patient_id = str(uuid.uuid4())[:8]

    timestamp = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    patient_df = pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "Age": [age]
    })

    # Call src modules
    prediction, probability = predict_diabetes(patient_df)

    risk_score = calculate_risk_score(
        glucose,
        bmi,
        age
    )

    cluster, recommendation = generate_recommendation(
        risk_score
    )

    alerts = generate_alerts(
        glucose,
        bmi,
        insulin
    )

    st.divider()

    st.header("📊 Patient Risk Assessment")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Risk Score",
            risk_score
        )

    with c2:
        st.metric(
            "Diabetes Probability",
            f"{probability:.2f}%"
        )

    with c3:
        st.metric(
            "Risk Cluster",
            cluster
        )

    if cluster == "High Risk":
        st.error(cluster)

    elif cluster == "Medium Risk":
        st.warning(cluster)

    else:
        st.success(cluster)

    st.success(recommendation)

    st.subheader("📋 Executive Summary")

    st.write(
        f"""
Patient Name: {patient_name}

Patient ID: {patient_id}

Generated On: {timestamp}

Risk Score: {risk_score}

Diabetes Probability: {probability:.2f}%

Risk Category: {cluster}
"""
    )

    st.subheader("🚨 Alerts")

    if alerts:
        for alert in alerts:
            st.warning(alert)
    else:
        st.success(
            "No critical alerts detected."
        )

    doctor_notes = """
This report is AI-generated and intended
for preliminary health assessment only.
Consult a licensed physician for
medical decisions.
"""

    pdf_path = f"reports/{patient_id}.pdf"

    generate_pdf(
        filename=pdf_path,
        patient_name=patient_name,
        patient_id=patient_id,
        timestamp=timestamp,
        age=age,
        bmi=bmi,
        glucose=glucose,
        blood_pressure=blood_pressure,
        insulin=insulin,
        risk_score=risk_score,
        cluster=cluster,
        probability=probability,
        recommendation=recommendation,
        alerts=alerts,
        doctor_notes=doctor_notes
    )

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            label="📄 Download Medical Report",
            data=pdf_file,
            file_name=f"Patient_Report_{patient_id}.pdf",
            mime="application/pdf"
        )