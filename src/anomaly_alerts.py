import pandas as pd


def generate_alerts(df):

    alerts = []

    for _, row in df.iterrows():

        patient_alerts = []

        if row["Insulin"] > 318:
            patient_alerts.append(
                "Critical Insulin Anomaly"
            )

        if row["Glucose"] > 180:
            patient_alerts.append(
                "Very High Glucose"
            )

        if row["BMI"] > 40:
            patient_alerts.append(
                "Severe Obesity Risk"
            )

        if len(patient_alerts) == 0:
            alerts.append("No Alert")

        else:
            alerts.append(
                " | ".join(patient_alerts)
            )

    df["Alert"] = alerts

    return df

def generate_alerts(
    glucose,
    bmi,
    insulin
):

    alerts = []

    if glucose > 180:
        alerts.append(
            "Very High Glucose Detected"
        )

    if bmi > 40:
        alerts.append(
            "Severe Obesity Risk"
        )

    if insulin > 318:
        alerts.append(
            "Critical Insulin Anomaly"
        )

    return alerts


if __name__ == "__main__":

    df = pd.read_csv(
        "../data/processed/patient_recommendations.csv"
    )

    df = generate_alerts(df)

    df.to_csv(
        "../data/processed/cleaned_patients.csv",
        index=False
    )

    print("Alerts generated!")