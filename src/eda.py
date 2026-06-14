import matplotlib.pyplot as plt
import seaborn as sns


def age_distribution(df):
    plt.figure(figsize=(8, 5))

    plt.hist(df["Age"], bins=15)

    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


def glucose_vs_outcome(df):
    plt.figure(figsize=(8, 5))

    sns.boxplot(
        x="Outcome",
        y="Glucose",
        data=df
    )

    plt.title("Glucose vs Outcome")
    plt.xlabel("Outcome (0 = No Diabetes, 1 = Diabetes)")
    plt.ylabel("Glucose")

    plt.tight_layout()
    plt.show()


def bmi_distribution(df):
    plt.figure(figsize=(8, 5))

    plt.hist(df["BMI"], bins=20)

    plt.title("BMI Distribution")
    plt.xlabel("BMI")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


def correlation_heatmap(df):
    plt.figure(figsize=(10, 8))

    corr = df.corr(numeric_only=True)

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()
    plt.show()