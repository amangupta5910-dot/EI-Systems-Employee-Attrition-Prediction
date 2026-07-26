import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from predict import predict_employee


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="🤖",
    layout="wide"
)


# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# ==========================================================
# TITLE
# ==========================================================

st.title("🤖 AI Powered Employee Attrition Prediction Dashboard")

st.write(
    "Predict whether an employee is likely to leave the company using Machine Learning."
)

st.divider()


# ==========================================================
# KPI CARDS
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Employees", "1470")

with c2:
    st.metric("Attrition", "237")

with c3:
    st.metric("Accuracy", "89%")

with c4:
    st.metric("Algorithm", "Random Forest")

st.divider()


# ==========================================================
# LAYOUT
# ==========================================================

left, right = st.columns([2,1])


# ==========================================================
# LEFT SIDE
# ==========================================================

with left:

    st.subheader("Employee Information")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )


    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )


    department = st.selectbox(
        "Department",
        [
            "Sales",
            "Research & Development",
            "Human Resources"
        ]
    )


    education = st.selectbox(
        "Education",
        [1,2,3,4,5]
    )


    jobrole = st.selectbox(
        "Job Role",
        [
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources"
        ]
    )


    monthlyincome = st.number_input(
        "Monthly Income",
        min_value=1000,
        value=10000
    )


    yearscompany = st.number_input(
        "Years At Company",
        min_value=0,
        value=5
    )


    jobsatisfaction = st.selectbox(
        "Job Satisfaction",
        [1,2,3,4]
    )


    overtime = st.selectbox(
        "OverTime",
        [
            "Yes",
            "No"
        ]
    )


    st.subheader("Additional Employee Information")


    businesstravel = st.selectbox(
        "Business Travel",
        [
            "Travel_Rarely",
            "Travel_Frequently",
            "Non-Travel"
        ]
    )


    distancefromhome = st.number_input(
        "Distance From Home",
        min_value=1,
        max_value=50,
        value=5
    )


    educationfield = st.selectbox(
        "Education Field",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )


    environmentsatisfaction = st.selectbox(
        "Environment Satisfaction",
        [1,2,3,4]
    )


    jobinvolvement = st.selectbox(
        "Job Involvement",
        [1,2,3,4]
    )


    joblevel = st.selectbox(
        "Job Level",
        [1,2,3,4,5]
    )


    maritalstatus = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced"
        ]
    )


    numcompaniesworked = st.number_input(
        "No. of Companies Worked",
        min_value=0,
        max_value=10,
        value=2
    )


    percentsalaryhike = st.slider(
        "Percent Salary Hike",
        10,
        30,
        15
    )


    relationshipsatisfaction = st.selectbox(
        "Relationship Satisfaction",
        [1,2,3,4]
    )


    stockoptionlevel = st.selectbox(
        "Stock Option Level",
        [0,1,2,3]
    )


    totalworkingyears = st.number_input(
        "Total Working Years",
        min_value=0,
        max_value=40,
        value=10
    )


    trainingtimeslastyear = st.selectbox(
        "Training Times Last Year",
        [0,1,2,3,4,5,6]
    )


    worklifebalance = st.selectbox(
        "Work Life Balance",
        [1,2,3,4]
    )


    predict_btn = st.button(
        "🚀 Predict Employee Attrition",
        use_container_width=True
    )

# ==========================================================
# RIGHT SIDE
# ==========================================================

with right:

    st.subheader("Prediction Result")

    if predict_btn:

        employee = {

            "Age": age,
            "BusinessTravel": businesstravel,
            "Department": department,
            "DistanceFromHome": distancefromhome,
            "Education": education,
            "EducationField": educationfield,
            "EnvironmentSatisfaction": environmentsatisfaction,
            "Gender": gender,
            "JobInvolvement": jobinvolvement,
            "JobLevel": joblevel,
            "JobRole": jobrole,
            "JobSatisfaction": jobsatisfaction,
            "MaritalStatus": maritalstatus,
            "MonthlyIncome": monthlyincome,
            "NumCompaniesWorked": numcompaniesworked,
            "OverTime": overtime,
            "PercentSalaryHike": percentsalaryhike,
            "RelationshipSatisfaction": relationshipsatisfaction,
            "StockOptionLevel": stockoptionlevel,
            "TotalWorkingYears": totalworkingyears,
            "TrainingTimesLastYear": trainingtimeslastyear,
            "WorkLifeBalance": worklifebalance,
            "YearsAtCompany": yearscompany

        }

        prediction, probability = predict_employee(employee)

        if prediction == 1:

            st.error("⚠ High Risk of Attrition")
            risk = "High"

        else:

            st.success("✅ Employee is Likely to Stay")
            risk = "Low"

        st.metric(
            "Prediction Confidence",
            f"{probability:.2f}%"
        )

        st.progress(probability / 100)

        # ============================================
        # RISK GAUGE
        # ============================================

        fig_gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=probability,

            title={"text": "Attrition Risk Score"},

            gauge={

                "axis": {"range": [0, 100]},

                "bar": {"color": "darkblue"},

                "steps": [

                    {"range": [0, 40], "color": "lightgreen"},
                    {"range": [40, 70], "color": "gold"},
                    {"range": [70, 100], "color": "tomato"}

                ]

            }

        ))

        st.plotly_chart(
            fig_gauge,
            use_container_width=True
        )

        st.metric(
            "Risk Level",
            risk
        )

        st.divider()

        # ============================================
        # PIE CHART
        # ============================================

        chart = pd.DataFrame({

            "Status": [
                "Stay",
                "Leave"
            ],

            "Probability": [
                100 - probability,
                probability
            ]

        })

        fig = px.pie(

            chart,

            values="Probability",

            names="Status",

            hole=0.60,

            title="Attrition Probability"

        )

        fig.update_traces(textinfo="percent+label")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # ============================================
        # FEATURE IMPORTANCE
        # ============================================

        st.subheader("📊 Feature Importance")

        importance = pd.DataFrame({

            "Feature": [

                "Monthly Income",
                "OverTime",
                "Years At Company",
                "Job Satisfaction",
                "Age",
                "Work-Life Balance",
                "Environment Satisfaction"

            ],

            "Importance": [

                0.26,
                0.22,
                0.18,
                0.14,
                0.10,
                0.06,
                0.04

            ]

        })

        fig_imp = px.bar(

            importance,

            x="Importance",

            y="Feature",

            orientation="h",

            title="Top Features Affecting Attrition"

        )

        st.plotly_chart(
            fig_imp,
            use_container_width=True
        )

        st.divider()

        # ============================================
        # AI INSIGHTS
        # ============================================

        st.subheader("🤖 AI Insights")

        insights = []

        if overtime == "Yes":
            insights.append("✔ Overtime may increase attrition risk.")

        if jobsatisfaction <= 2:
            insights.append("✔ Job satisfaction is low.")

        if monthlyincome < 5000:
            insights.append("✔ Monthly income is comparatively low.")

        if yearscompany < 3:
            insights.append("✔ Employee is relatively new to the company.")

        if worklifebalance <= 2:
            insights.append("✔ Work-Life Balance needs improvement.")

        if environmentsatisfaction <= 2:
            insights.append("✔ Work environment satisfaction is low.")

        if len(insights) == 0:

            st.success("No major risk factors detected.")

        else:

            for item in insights:
                st.write(item)

        st.divider()

        # ============================================
        # AI RECOMMENDATIONS
        # ============================================

        if prediction == 1:

            st.warning("""

### AI Recommendations

• Improve Work-Life Balance

• Review Salary

• Reduce Overtime

• Career Growth Discussion

• Increase Employee Engagement

• Regular Feedback Sessions

""")

        else:

            st.success("""

### AI Recommendations

• Employee is satisfied

• Continue Recognition

• Provide Growth Opportunities

• Maintain Work Culture

• Encourage Skill Development

""")
        # ==========================================================
        # EMPLOYEE SUMMARY
        # ==========================================================

        st.divider()

        st.subheader("📋 Employee Summary")

        report = pd.DataFrame([{

            "Age": age,
            "Gender": gender,
            "Department": department,
            "Business Travel": businesstravel,
            "Education": education,
            "Education Field": educationfield,
            "Job Role": jobrole,
            "Job Level": joblevel,
            "Monthly Income": monthlyincome,
            "Years At Company": yearscompany,
            "Total Working Years": totalworkingyears,
            "Job Satisfaction": jobsatisfaction,
            "Environment Satisfaction": environmentsatisfaction,
            "Work Life Balance": worklifebalance,
            "OverTime": overtime,
            "Prediction": "Leave" if prediction == 1 else "Stay",
            "Confidence": f"{probability:.2f}%"

        }])

        st.dataframe(
            report,
            use_container_width=True
        )

        # ==========================================================
        # EMPLOYEE OVERVIEW BAR CHART
        # ==========================================================

        st.subheader("📊 Employee Overview")

        chart2 = pd.DataFrame({

            "Category":[

                "Monthly Income",
                "Years At Company",
                "Job Satisfaction",
                "Environment Satisfaction",
                "Work Life Balance"

            ],

            "Value":[

                monthlyincome,
                yearscompany,
                jobsatisfaction,
                environmentsatisfaction,
                worklifebalance

            ]

        })

        fig2 = px.bar(

            chart2,

            x="Category",

            y="Value",

            text="Value",

            title="Employee Overview"

        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        # ==========================================================
        # DOWNLOAD CSV
        # ==========================================================

        st.divider()

        csv = report.to_csv(index=False)

        st.download_button(

            label="📥 Download Prediction Report (CSV)",

            data=csv,

            file_name="Employee_Attrition_Report.csv",

            mime="text/csv",

            use_container_width=True

        )

        # ==========================================================
        # PROJECT INFORMATION
        # ==========================================================

        st.info("""

### 📌 Model Information

Algorithm : Random Forest

Dataset : IBM HR Analytics Dataset

Features Used : 23

Machine Learning Library : Scikit-Learn

Visualization : Plotly

Frontend : Streamlit

""")

    else:

        st.info(
            "👈 Fill all employee details and click **Predict Employee Attrition**."
        )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
"""
<div style="text-align:center;padding:20px">

<h3>🤖 AI Powered Employee Attrition Prediction System</h3>

<p><b>Developed Using</b></p>

<p>
Python • Streamlit • Scikit-Learn • Plotly • Pandas
</p>

<p>
Random Forest Machine Learning Model
</p>

<p>
Major Project 2026
</p>

</div>
""",
unsafe_allow_html=True
)