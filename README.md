# 🏥 Diabetes Risk Intelligence System

## Overview
Diabetes Risk Intelligence System is an AI-powered healthcare analytics and risk assessment platform built using Python, Machine Learning, and Streamlit. 

The system analyzes patient health metrics, predicts diabetes risk, generates personalized risk scores, detects anomalies, provides medical recommendations, and automatically generates downloadable PDF medical reports.

The project combines data preprocessing, exploratory data analysis (EDA), clustering, risk scoring, machine learning prediction, anomaly detection, and interactive report generation into a single end-to-end healthcare intelligence solution.

---

## Live Demo

Experience the application live:

* **Streamlit Application:** [diabetes-risk-intelligence-system](https://diabetes-risk-intelligence-system.streamlit.app/)

---

## GitHub Repository

Source code and project documentation:

* **GitHub Repository:** [bhuvaneshwarid48/diabetes-risk-intelligence](https://github.com/Bhuvaneshwari-Dhanabal/diabetes-risk-intelligence-system)

---

## Dataset

### Pima Indians Diabetes Dataset
* **Source:** [Kaggle - Pima Indians Diabetes Database](https://kaggle.com)

---

## Project Structure

```text
patient-risk-intelligence/
│
├── app.py                               # Streamlit application
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── logo.jpg                         # Hospital/Project logo
│
├── data/
│   ├── raw/
│   │   └── diabetes.csv                 # Original dataset
│   │
│   └── processed/
│       ├── cleaned_patients.csv
│       ├── patient_clusters.csv
│       ├── patient_predictions.csv
│       ├── patient_recommendations.csv
│       └── patient_risk_clusters.png
│
├── models/
│   └── diabetes_rf.pkl                  # Trained Random Forest model
│
├── notebooks/
│   └── patient_EDA.ipynb                # EDA notebook
│
├── reports/
│   └── *.pdf                            # Generated patient reports
│
├── Screenshots/
│   ├── home_page.png
│   ├── report_section.png
│   ├── sample_pdf.png
│   └── save_pdf.png
│
├── src/
│   ├── preprocess.py                    # Data cleaning & feature engineering
│   ├── eda.py                           # Exploratory Data Analysis
│   ├── outlier_detection.py             # IQR-based anomaly detection
│   ├── clustering.py                    # K-Means patient segmentation
│   ├── risk_scoring.py                  # Custom risk score calculation
│   ├── diabetes_prediction.py           # Random Forest prediction
│   ├── recommendation_engine.py         # Personalized recommendations
│   ├── anomaly_alerts.py                # Critical health alerts
│   └── pdf_report.py                    # Medical PDF report generation
│
└── Visualizations/
    ├── age_distribution.png
    ├── BMI_distributions.png
    ├── Correlation_Heatmap.png
    └── Glucose_outcome_boxplot.png
```

---

## Features

### 🛠️ Data Engineering
* Data Cleaning
* Missing Value Imputation
* Age Band Creation
* BMI Category Generation
* Feature Engineering

### 📊 Exploratory Data Analysis
* Age Distribution Analysis
* BMI Distribution Analysis
* Glucose vs Outcome Analysis
* Correlation Heatmap

### 🔍 Outlier Detection
* IQR-based Outlier Detection
* Insulin Anomaly Identification

### 🤖 Machine Learning
* Random Forest Diabetes Prediction Model
* Diabetes Probability Estimation
* Risk Classification

### 🧠 Risk Intelligence Engine
* Custom Risk Score Calculation
* Low / Medium / High Risk Categorization
* Patient Risk Segmentation
* Personalized Health Assessment

### 📋 Recommendation System
* Automated Health Recommendations
* Risk-based Action Suggestions
* Preventive Care Guidance

### 🚨 Alert System
* High Glucose Detection
* Severe Obesity Detection
* Critical Insulin Anomaly Detection

### 📄 Medical Report Generation
* Hospital-style PDF Report
* Patient Health Summary
* Risk Assessment Report
* Doctor Notes Section
* Downloadable PDF Reports

### 💻 Interactive Dashboard
* Streamlit Frontend
* Real-time Patient Assessment
* Interactive Input Forms
* One-click Report Generation

---

## Workflow

```text
Patient Input
      ↓
Data Validation
      ↓
Diabetes Prediction Model
      ↓
Risk Score Calculation
      ↓
Risk Classification
      ↓
Recommendation Engine
      ↓
Anomaly Detection
      ↓
Medical Report Generation
      ↓
PDF Download
```

---

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model
```bash
python src/diabetes_prediction.py
```

### 3. Launch Streamlit Application
```bash
streamlit run app.py
```

---

## Key Insights
* Glucose is the strongest predictor of diabetes risk.
* BMI has a significant impact on diabetes probability.
* Most patients fall into overweight or obese BMI categories.
* Insulin contains several extreme outliers requiring investigation.
* K-Means clustering successfully identifies patient risk groups.
* Machine learning prediction improves risk assessment accuracy.

---

## Visualizations

### Correlation Heatmap
![Correlation Heatmap](/Visualizations/Correlation_Heatmap.png)

### Glucose vs Outcome Boxplot
![Glucose vs Outcome Boxplot](/Visualizations/Glucose_outcome_boxplot.png)

### Age Distribution Histogram
![Age Distribution Histogram](/Visualizations/age_distribution.png)

### BMI Distribution Histogram
![BMI Distribution Histogram](/Visualizations/BMI_distributions.png)

---

## Screenshots

### Streamlit Dashboard
![Streamlit Dashboard](/Screenshots/home_page.png)

![Streamlit Dashboard](/Screenshots/report_section.png)

### Generated Medical Report
![Generated Medical Report](/Screenshots/sample_pdf.png)

---

## Sample Output

### Patient Risk Assessment
* Diabetes Probability
* Risk Score
* Risk Cluster
* Personalized Recommendation
* Health Alerts

### Generated Medical Report
* Patient Information
* Health Assessment Summary
* Risk Analysis
* Recommendation Section
* Doctor Notes
* PDF Download

---

## Technologies Used
* **Languages:** Python
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn, Joblib
* **Deployment & UI:** Streamlit
* **Reporting:** ReportLab

---

## Future Enhancements
* Multi-Disease Prediction
* Doctor Login Portal
* Patient History Tracking
* Cloud Deployment (AWS)
* Real-time Database Integration
* Email Report Delivery
* AI Chat Assistant for Patients

---

## Author 🧬

### Bhuvaneshwari D
**Aspiring Data Analyst | Python Developer | Cloud & AI Enthusiast**  
**GitHub:** [@Bhuvaneshwari-Dhanabal](https://github.com/Bhuvaneshwari-Dhanabal)
