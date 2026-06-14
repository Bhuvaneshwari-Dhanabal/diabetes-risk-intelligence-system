import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def calculate_risk_score(df):
    """
    Risk Score Formula:
    (Glucose × 0.4) + (BMI × 0.3) + (Age × 0.3)

    Normalize to 0–100
    """

    df["RawRiskScore"] =(
    df["Glucose"] * 0.35 +
    df["BMI"] * 0.20 +
    df["Age"] * 0.10 +
    df["BloodPressure"] * 0.15 +
    df["Insulin"] * 0.10 +
    df["Pregnancies"] * 0.10
)
    scaler = MinMaxScaler(feature_range=(0, 100))

    df["RiskScore"] = scaler.fit_transform(
        df[["RawRiskScore"]]
    )

    df["RiskScore"] = min(round(df["RiskScore"].iloc[0] / 2.5, 2), 100)

    return df

def calculate_risk_score(glucose, bmi, age):

    score = (
        glucose * 0.4 +
        bmi * 0.3 +
        age * 0.3
    )

    score = min(
        round(score / 2, 2),
        100
    )

    return score

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/patient_clusters.csv")

    df = calculate_risk_score(df)

    df.to_csv(
        "../data/processed/patient_risk_scores.csv",
        index=False
    )

    print("Risk scores generated successfully!")
    print(df[["Glucose", "BMI", "Age", "RiskScore"]].head())