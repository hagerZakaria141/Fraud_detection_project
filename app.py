import streamlit as st
import requests
import base64

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(page_title="Fraud Detection", layout="wide")

# ======================
# BACKGROUND IMAGE
# ======================
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("background.jpg")

# ======================
# STYLE
# ======================
st.markdown(f"""
<style>

/* ===== FULL BACKGROUND ===== */
.stApp {{
    background-image: linear-gradient(
        rgba(0,0,0,0.6),
        rgba(0,0,0,0.6)
    ),
    url("data:image/jpg;base64,{img}");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* ===== CENTER LAYOUT WIDTH CONTROL ===== */
.block-container {{
    max-width: 900px;
    padding-top: 2rem;
}}

/* ===== TEXT COLOR ===== */
h1, h2, h3, p, label {{
    color: #f5f5f5 !important;
}}

/* ===== CARD STYLE ===== */
.card {{
    background: rgba(255, 255, 255, 0.10);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(8px);
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    color: white;
    margin-bottom: 15px;
}}

/* ===== INPUT WIDTH CONTROL ===== */
.stTextInput, .stNumberInput, .stSelectbox {{
    max-width: 400px;
}}

/* ===== BUTTON ===== */
.stButton>button {{
    background-color: #6b7f5b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}}

.stButton>button:hover {{
    background-color: #4f6244;
}}

/* ===== RESULT BOX ===== */
.result-box {{
    background: rgba(0,0,0,0.5);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
}}

</style>
""", unsafe_allow_html=True)

# ======================
# TITLE
# ======================
st.title("Insurance Fraud Detection System")
st.write("Fill details to predict fraud risk")

# ======================
# TABS
# ======================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Policy Info",
    "👤 Insured Info",
    "🚨 Incident Info",
    "📅 Date Info"
])

# ----------------------
# TAB 1
# ----------------------
with tab1:
    policy_state = st.text_input("Policy State")
    policy_deductible = st.number_input("Policy Deductible", 500)
    policy_annual_premium = st.number_input("Annual Premium", 1200)
    claim_amount = st.number_input("Claim Amount", 0)
    total_claim_amount = st.number_input("Total Claim Amount", 0)

# ----------------------
# TAB 2
# ----------------------
with tab2:
    insured_age = st.number_input("Age", 30)
    insured_sex = st.selectbox("Sex", ["Male", "Female"])
    insured_education_level = st.text_input("Education Level")
    insured_occupation = st.text_input("Occupation")
    insured_hobbies = st.text_input("Hobbies")

# ----------------------
# TAB 3
# ----------------------
with tab3:
    incident_type = st.text_input("Incident Type")
    collision_type = st.text_input("Collision Type")
    incident_severity = st.text_input("Incident Severity")
    authorities_contacted = st.text_input("Authorities Contacted")
    incident_state = st.text_input("Incident State")

    incident_hour_of_the_day = st.number_input("Incident Hour", 0, 23)
    number_of_vehicles_involved = st.number_input("Vehicles Involved", 1)
    bodily_injuries = st.number_input("Bodily Injuries", 0)
    witnesses = st.number_input("Witnesses", 0)

    police_report_available = st.selectbox("Police Report Available", ["Yes", "No"])

# ----------------------
# TAB 4
# ----------------------
with tab4:
    year = st.number_input("Year", 2024)
    month = st.number_input("Month", 1, 12)
    day = st.number_input("Day", 1, 31)
    day_of_week = st.number_input("Day of Week", 0, 6)

# ======================
# PREDICT
# ======================
if st.button("🔍 Predict Fraud"):

    with st.spinner("Analyzing data... 🤖"):

        url = "http://127.0.0.1:8000/predict"
        payload = {
            "policy_state": policy_state,
            "policy_deductible": policy_deductible,
            "policy_annual_premium": policy_annual_premium,
            "insured_age": insured_age,
            "insured_sex": insured_sex,
            "insured_education_level": insured_education_level,
            "insured_occupation": insured_occupation,
            "insured_hobbies": insured_hobbies,
            "incident_type": incident_type,
            "collision_type": collision_type,
            "incident_severity": incident_severity,
            "authorities_contacted": authorities_contacted,
            "incident_state": incident_state,
            "incident_hour_of_the_day": incident_hour_of_the_day,
            "number_of_vehicles_involved": number_of_vehicles_involved,
            "bodily_injuries": bodily_injuries,
            "witnesses": witnesses,
            "police_report_available": police_report_available,
            "claim_amount": claim_amount,
            "total_claim_amount": total_claim_amount,
            "year": year,
            "month": month,
            "day": day,
            "day_of_week": day_of_week
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                result = response.json()
                prediction = result["prediction"]

                st.markdown("---")
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)

                st.subheader("Prediction Result")

                if prediction == 1:
                    st.error("🚨 FRAUD DETECTED")
                    st.markdown("### ⚠ High Risk Case")
                else:
                    st.success("NOT FRAUD")
                    st.markdown("### Low Risk Case")

                st.markdown("</div>", unsafe_allow_html=True)

            else:
                st.error("API Error")

        except Exception as e:
            st.error(f"Connection Error: {e}")