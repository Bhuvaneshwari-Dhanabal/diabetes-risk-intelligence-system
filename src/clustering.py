import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


def run_clustering(df):
    features = ["Glucose", "BMI", "Age"]

    # Scale features
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(df[features])

    # KMeans clustering
    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    df["Cluster"] = kmeans.fit_predict(X_scaled)

    # Cluster centers
    centers = scaler.inverse_transform(kmeans.cluster_centers_)

    cluster_summary = pd.DataFrame(
        centers,
        columns=features
    )

    print("\nCluster Centers:")
    print(cluster_summary)

    # Sort clusters by risk level
    risk_order = (
        cluster_summary["Glucose"] +
        cluster_summary["BMI"] +
        cluster_summary["Age"]
    ).sort_values().index

    risk_map = {
        risk_order[0]: "Low Risk",
        risk_order[1]: "Medium Risk",
        risk_order[2]: "High Risk"
    }

    df["RiskGroup"] = df["Cluster"].map(risk_map)

    print("\nRisk Group Counts:")
    print(df["RiskGroup"].value_counts())

    return df, cluster_summary


def plot_clusters(df):
    plt.figure(figsize=(10, 6))

    colors = {
        "Low Risk": "green",
        "Medium Risk": "orange",
        "High Risk": "red"
    }

    for group in colors:
        subset = df[df["RiskGroup"] == group]

        plt.scatter(
            subset["Age"],
            subset["Glucose"],
            label=group,
            alpha=0.7
        )

    plt.title("Patient Risk Clusters")
    plt.xlabel("Age")
    plt.ylabel("Glucose")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "../data/processed/patient_risk_clusters.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("../data/processed/cleaned_patients.csv")

    df, centers = run_clustering(df)

    plot_clusters(df)

    df.to_csv(
        "../data/processed/patient_clusters.csv",
        index=False
    )

    print("\nClustered dataset saved.")