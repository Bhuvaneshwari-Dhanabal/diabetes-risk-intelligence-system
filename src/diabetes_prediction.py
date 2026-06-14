import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib


def train_diabetes_model(df):
    features = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "Age"
    ]

    X = df[features]
    y = df["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print(f"Model Accuracy: {accuracy:.2%}")

    df["Prediction"] = model.predict(X)

    
    joblib.dump(
    model,
    "../models/diabetes_rf.pkl"
) 
    return df, model


model = joblib.load(
    "models/diabetes_rf.pkl"
)

def predict_diabetes(patient_df):

    prediction = model.predict(
        patient_df
    )[0]

    probability = (
        model.predict_proba(patient_df)[0][1]
        * 100
    )

    return prediction, probability

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/cleaned_patients.csv")

    df, model = train_diabetes_model(df)

    df.to_csv(
        "../data/processed/patient_predictions.csv",
        index=False
    )

    print("Predictions saved successfully!")