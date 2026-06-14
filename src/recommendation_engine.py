import pandas as pd


def generate_recommendations(df):

    recommendations = []

    for _, row in df.iterrows():

        score = row["RiskScore"]

        if score >= 80:
            recommendations.append(
                "Immediate physician consultation"
            )

        elif score >= 60:
            recommendations.append(
                "Lifestyle intervention and glucose monitoring"
            )

        elif score >= 40:
            recommendations.append(
                "Regular health checkup recommended"
            )

        else:
            recommendations.append(
                "Maintain healthy lifestyle"
            )

    df["Recommendation"] = recommendations

    return df

def generate_recommendation(risk_score):

    if risk_score >= 80:

        return (
            "High Risk",
            "Immediate physician consultation recommended."
        )

    elif risk_score >= 60:

        return (
            "Medium Risk",
            "Lifestyle intervention and glucose monitoring recommended."
        )

    else:

        return (
            "Low Risk",
            "Maintain healthy lifestyle."
        )
    
    
if __name__ == "__main__":

    df = pd.read_csv("../data/processed/patient_predictions.csv")

    df = generate_recommendations(df)

    df.to_csv(
        "../data/processed/patient_recommendations.csv",
        index=False
    )

    print("Recommendations generated!")