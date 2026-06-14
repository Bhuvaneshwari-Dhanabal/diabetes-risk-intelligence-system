from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image
from reportlab.platypus import PageBreak
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle

def generate_pdf(
    filename,
    patient_name,
    patient_id,
    timestamp,
    age,
    bmi,
    glucose,
    blood_pressure,
    insulin,
    risk_score,
    cluster,
    probability,
    recommendation,
    alerts,
    doctor_notes
):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []
    logo_path = "assets/logo.jpg"

    logo = Image(
    logo_path,
    width=100,
    height=100
    )

    elements.append(logo)
    elements.append(Spacer(1, 10))
    elements.append(
        Paragraph(
            "DIABETES RISK INTELLIGENCE REPORT",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"Patient Name: {patient_name}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Patient ID: {patient_id}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Generated On: {timestamp}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            "Clinical Measurements",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Age: {age}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"BMI: {bmi}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Glucose: {glucose}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Blood Pressure: {blood_pressure}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Insulin: {insulin}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            "Risk Assessment",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Risk Score: {risk_score}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Risk Cluster: {cluster}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Diabetes Probability: {probability:.2f}%",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Recommendation: {recommendation}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            "Alerts",
            styles["Heading2"]
        )
    )

    if alerts:
        for alert in alerts:
            elements.append(
                Paragraph(
                    alert,
                    styles["BodyText"]
                )
            )
    else:
        elements.append(
            Paragraph(
                "No alerts detected.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 12))

    

   
    elements.append(PageBreak())
    elements.append(
    Paragraph(
    "Patient Health Summary",
    styles["Title"]
)
)

    elements.append(Spacer(1,15))

    kpi_data = [

    ["Metric", "Value", "Status"],

    ["Age", age, "Normal"],

    ["Glucose",
     glucose,
     "High" if glucose > 140 else "Normal"],

    ["BMI",
     bmi,
     "High" if bmi > 30 else "Normal"],

    ["Blood Pressure",
     blood_pressure,
     "High" if blood_pressure > 80 else "Normal"],

    ["Insulin",
     insulin,
     "High" if insulin > 318 else "Normal"],

    ["Risk Score",
     risk_score,
     cluster]
]

    kpi_table = Table(kpi_data)
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(kpi_table)

    elements.append(Spacer(1,20))

    summary = f"""
Patient exhibits a risk score of {risk_score}
and falls under the {cluster} category and the predicted diabetes probability is 
{probability:.2f}%, which indicates a {cluster.lower()} risk of developing diabetes.
Based on the reported clinical measurements and risk assessment, the following recommendation is provided as 
{recommendation}
"""

    elements.append(
    Paragraph(
        summary,
        styles["BodyText"]
    )
)
    
    elements.append(
        Paragraph(
            "Doctor Notes",
            styles["Heading2"]
        )
    )
    elements.append(
        Paragraph(
            doctor_notes,
            styles["BodyText"]
        )
    )
    thank_style = ParagraphStyle(
    "ThankYouStyle",
    parent=styles["BodyText"],
    alignment=TA_CENTER,
    fontSize=12,
    leading=18
)
    elements.append(Spacer(1, 120))
    elements.append(
    Paragraph(
        """
        <b>Thank You for Using Our Patient Risk Intelligence System</b>
        <br/><br/>
        We hope this report provides helpful insights into your current health status.
        <br/><br/>
        Wishing you good health, a speedy recovery, and a healthier future ahead.
        <br/><br/>
        Stay positive, stay healthy, and take care.
        """,
        thank_style
    )
)
    pdf.build(elements)