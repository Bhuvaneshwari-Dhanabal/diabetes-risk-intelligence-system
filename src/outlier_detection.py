import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def detect_insulin_outliers(df):
    """
    Detect outliers in Insulin column using IQR method.
    """

    Q1 = df["Insulin"].quantile(0.25)
    Q3 = df["Insulin"].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df["Insulin"] = df["Insulin"].replace(0, np.nan)
    df["Insulin"] = df["Insulin"].fillna(df["Insulin"].median())
    df["Insulin_Outlier"] = (
        (df["Insulin"] < lower_bound) |
        (df["Insulin"] > upper_bound)
    )

    outlier_count = df["Insulin_Outlier"].sum()

    print(f"Q1: {Q1}")
    print(f"Q3: {Q3}")
    print(f"IQR: {IQR}")
    print(f"Lower Bound: {lower_bound}")
    print(f"Upper Bound: {upper_bound}")
    print(f"Number of Outliers: {outlier_count}")

    return df, outlier_count

def plot_insulin_boxplot(df):
    plt.figure(figsize=(10, 5))

    plt.boxplot(
        df["Insulin"],
        vert=False,
        showfliers=True,  # hide outlier points
        showmeans=True
    )

    plt.title("Insulin Distribution")
    plt.xlabel("Insulin")
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.show()


def insulin_distribution(df):
    plt.figure(figsize=(10, 5))

    plt.hist(df["Insulin"], bins=30)

    plt.title("Insulin Distribution")
    plt.xlabel("Insulin")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("../data/processed/cleaned_patients.csv")

    df, outlier_count = detect_insulin_outliers(df)

    print("\nTotal Outliers:", outlier_count)
    plot_insulin_boxplot(df)
    insulin_distribution(df)