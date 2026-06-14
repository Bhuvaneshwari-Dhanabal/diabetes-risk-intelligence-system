import pandas as pd
import numpy as np

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    cols = ["Glucose", "BloodPressure", "BMI"]

    # Convert 0 to NaN
    df[cols] = df[cols].replace(0, np.nan)

    # Median imputation
    for col in cols:
        df[col] = df[col].fillna(df[col].median())

    # Age Band
    age_bins = [20, 30, 40, 50, float('inf')]
    age_labels = ["20-30", "30-40", "40-50", "50+"]

    df["AgeBand"] = pd.cut(
        df["Age"],
        bins=age_bins,
        labels=age_labels,
        right=False
    )

    # BMI Category
    bmi_bins = [0, 18.5, 25, 30, float('inf')]
    bmi_labels = ["Underweight", "Normal", "Overweight", "Obese"]

    df["BMICategory"] = pd.cut(
        df["BMI"],
        bins=bmi_bins,
        labels=bmi_labels,
        right=False
    )

    return df


if __name__ == "__main__":
    df = load_data("../data/raw/diabetes.csv")
    df= preprocess_data(df)


    