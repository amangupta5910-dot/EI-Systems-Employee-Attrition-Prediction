import joblib
import pandas as pd

# -----------------------------
# Load Files
# -----------------------------
model = joblib.load("model/employee_attrition_model.pkl")
features = joblib.load("model/features.pkl")
encoders = joblib.load("model/label_encoders.pkl")


# -----------------------------
# Encoder Helper
# -----------------------------
def encode(feature, value):
    if feature in encoders:
        return encoders[feature].transform([value])[0]
    return value


# -----------------------------
# Prediction Function
# -----------------------------
def predict_employee(data):

    employee = {

        "Age": int(data["Age"]),

        "BusinessTravel": encode(
            "BusinessTravel",
            data["BusinessTravel"]
        ),

        "Department": encode(
            "Department",
            data["Department"]
        ),

        "DistanceFromHome": int(
            data["DistanceFromHome"]
        ),

        "Education": int(
            data["Education"]
        ),

        "EducationField": encode(
            "EducationField",
            data["EducationField"]
        ),

        "EnvironmentSatisfaction": int(
            data["EnvironmentSatisfaction"]
        ),

        "Gender": encode(
            "Gender",
            data["Gender"]
        ),

        "JobInvolvement": int(
            data["JobInvolvement"]
        ),

        "JobLevel": int(
            data["JobLevel"]
        ),

        "JobRole": encode(
            "JobRole",
            data["JobRole"]
        ),

        "JobSatisfaction": int(
            data["JobSatisfaction"]
        ),

        "MaritalStatus": encode(
            "MaritalStatus",
            data["MaritalStatus"]
        ),

        "MonthlyIncome": float(
            data["MonthlyIncome"]
        ),

        "NumCompaniesWorked": int(
            data["NumCompaniesWorked"]
        ),

        "OverTime": encode(
            "OverTime",
            data["OverTime"]
        ),

        "PercentSalaryHike": int(
            data["PercentSalaryHike"]
        ),

        "RelationshipSatisfaction": int(
            data["RelationshipSatisfaction"]
        ),

        "StockOptionLevel": int(
            data["StockOptionLevel"]
        ),

        "TotalWorkingYears": int(
            data["TotalWorkingYears"]
        ),

        "TrainingTimesLastYear": int(
            data["TrainingTimesLastYear"]
        ),

        "WorkLifeBalance": int(
            data["WorkLifeBalance"]
        ),

        "YearsAtCompany": int(
            data["YearsAtCompany"]
        )

    }

    df = pd.DataFrame([employee])

    df = df[features]

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0].max() * 100

    return prediction, probability
