import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ---------------------------------------------------
# 1. LOAD TRAINED MODEL
# ---------------------------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("my_model.pkl")
    return model

model = load_model()

# ---------------------------------------------------
# 2. HELPER: ENCODING FUNCTIONS FOR CATEGORICAL INPUTS
# ---------------------------------------------------

def encode_ordinal(value, mapping_dict):
    """
    Convert a category (e.g., 'Low') to a number using a dictionary.
    Example: {'Low': 0, 'Medium': 1, 'High': 2}
    """
    return mapping_dict[value]

# Mappings – MUST MATCH what you used during training
ordinal_lmh = {"Low": 0, "Medium": 1, "High": 2}
ordinal_distance = {"Near": 0, "Moderate": 1, "Far": 2}
ordinal_parent_edu = {"High School": 0, "College": 1, "Postgraduate": 2}
motivation_map = {"Low": 0, "Medium": 1, "High": 2}  # for Study_Motivation_Interaction

# ---------------------------------------------------
# 3. STREAMLIT PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Student Exam Score Predictor",
    page_icon="📚",
    layout="centered"
)

st.title("📊 Student Exam Score Predictor")
st.write("Enter the student information below to estimate the **final exam score**.")


# ---------------------------------------------------
# 4. SECTION 1 — STUDENT ACADEMIC BEHAVIOR
# ---------------------------------------------------
st.markdown("""
    <div style="padding:10px; border-radius:8px; 
    background-color:#EEF2FF; margin-bottom:20px;">
    <h3 style='margin:0; color:#3730A3;'>1. 🧠 Student Academic Behavior</h3>
    </div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    hours_studied = st.number_input(
        "Hours studied per week",
        min_value=0.0, max_value=80.0, value=10.0, step=1.0
    )

with col2:
    attendance = st.number_input(
        "Attendance percentage (%)",
        min_value=0.0, max_value=100.0, value=85.0, step=1.0
    )

col3, col4 = st.columns(2)

with col3:
    sleep_hours = st.number_input(
        "Sleep hours per day",
        min_value=0.0, max_value=24.0, value=7.0, step=0.5
    )

with col4:
    tutoring_sessions = st.number_input(
        "Tutoring sessions per month",
        min_value=0.0, max_value=30.0, value=0.0, step=1.0
    )

col5, col6 = st.columns(2)

with col5:
    physical_activity = st.number_input(
        "Physical activity per week (hours)",
        min_value=0.0, max_value=40.0, value=3.0, step=1.0
    )

with col6:
    extracurricular_yes_no = st.selectbox(
        "Participates in extracurricular activities?",
        ["No", "Yes"]
    )

motivation_level_str = st.selectbox(
    "Motivation level",
    ["Low", "Medium", "High"]
)

internet_access_str = st.selectbox(
    "Has internet access?",
    ["No", "Yes"]
)


# ---------------------------------------------------
# 5. SECTION 2 — FAMILY & HOME ENVIRONMENT
# ---------------------------------------------------
st.markdown("""
    <div style="padding:10px; border-radius:8px; 
    background-color:#EEF2FF; margin-bottom:20px;">
    <h3 style='margin:0; color:#3730A3;'>2. 🏠 Family & Home Environment</h3>
    </div>
""", unsafe_allow_html=True)


col7, col8 = st.columns(2)

with col7:
    family_income_str = st.selectbox(
        "Family income level",
        ["Low", "Medium", "High"]
    )

with col8:
    parental_involvement_str = st.selectbox(
        "Parental involvement",
        ["Low", "Medium", "High"]
    )

col9, col10 = st.columns(2)

with col9:
    parental_edu_str = st.selectbox(
        "Parental education level",
        ["High School", "College", "Postgraduate"]
    )

with col10:
    access_resources_str = st.selectbox(
        "Access to learning resources",
        ["Low", "Medium", "High"]
    )

col11, col12 = st.columns(2)

with col11:
    distance_from_home_str = st.selectbox(
        "Distance from home to school",
        ["Near", "Moderate", "Far"]
    )

with col12:
    learning_disabilities_str = st.selectbox(
        "Learning disabilities?",
        ["No", "Yes"]
    )


# ---------------------------------------------------
# 6. SECTION 3 — SCHOOL ENVIRONMENT
# ---------------------------------------------------
st.markdown("""
    <div style="padding:10px; border-radius:8px; 
    background-color:#EEF2FF; margin-bottom:20px;">
    <h3 style='margin:0; color:#3730A3;'>3. 🏫 School Environment</h3>
    </div>
""", unsafe_allow_html=True)

col13, col14 = st.columns(2)

with col13:
    teacher_quality_str = st.selectbox(
        "Teacher quality",
        ["Low", "Medium", "High"]
    )

with col14:
    school_type_str = st.selectbox(
        "School type",
        ["Public", "Private"]
    )

peer_influence_str = st.selectbox(
    "Peer influence",
    ["Negative", "Neutral", "Positive"]
)


# ---------------------------------------------------
# 7. SECTION 4 — PERSONAL PROFILE
# ---------------------------------------------------
st.markdown("""
    <div style="padding:10px; border-radius:8px; 
    background-color:#EEF2FF; margin-bottom:20px;">
    <h3 style='margin:0; color:#3730A3;'>4. 👤 Personal Profile</h3>
    </div>
""", unsafe_allow_html=True)

gender_str = st.selectbox(
    "Gender",
    ["Male", "Female"]
)


# ---------------------------------------------------
# 8. CONVERT USER INPUTS → NUMERIC FEATURES
# ---------------------------------------------------

# Binary encodings
internet_access = 1 if internet_access_str == "Yes" else 0
learning_disabilities = 1 if learning_disabilities_str == "Yes" else 0
extracurricular = 1 if extracurricular_yes_no == "Yes" else 0

female = 1 if gender_str == "Female" else 0
type_private = 1 if school_type_str == "Private" else 0
influence_positive = 1 if peer_influence_str == "Positive" else 0

# Ordinal encodings
family_income = encode_ordinal(family_income_str, ordinal_lmh)
parental_involvement = encode_ordinal(parental_involvement_str, ordinal_lmh)
access_to_resources = encode_ordinal(access_resources_str, ordinal_lmh)
teacher_quality = encode_ordinal(teacher_quality_str, ordinal_lmh)

distance_from_home = encode_ordinal(distance_from_home_str, ordinal_distance)
parental_education_level = encode_ordinal(parental_edu_str, ordinal_parent_edu)

motivation_level = encode_ordinal(motivation_level_str, motivation_map)

# Engineered features
study_motivation_interaction = hours_studied * motivation_level
parental_education_involvement = parental_education_level * parental_involvement

# ---------------------------------------------------
# 9. BUILD INPUT DATAFRAME FOR MODEL
# ---------------------------------------------------

# IMPORTANT: columns must match training features (names & order)
feature_dict = {
    "Parental_Involvement": parental_involvement,
    "Access_to_Resources": access_to_resources,
    "Family_Income": family_income,
    "Teacher_Quality": teacher_quality,
    "Distance_from_Home": distance_from_home,
    "Parental_Education_Level": parental_education_level,
    "Type_Private": type_private,
    "Influence_Positive": influence_positive,
    "Female": female,
    "Hours_Studied_Per_Week": hours_studied,
    "Attendance_Percentage": attendance,
    "Extracurricular_Activities": extracurricular,
    "Sleep_Hours": sleep_hours,
    "Internet_Access": internet_access,
    "Tutoring_Sessions_Per_Month": tutoring_sessions,
    "Physical_Activity_Per_Week": physical_activity,
    "Learning_Disabilities": learning_disabilities,
    "Study_Motivation_Interaction": study_motivation_interaction,
    "Parental_Education_Involvement": parental_education_involvement
}

input_df = pd.DataFrame([feature_dict])  # single row


# ---------------------------------------------------
# 10. PREDICT BUTTON
# ---------------------------------------------------
st.markdown("---")
if st.button("🔮 Predict Exam Score"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"Estimated Exam Score: **{prediction:.2f}** / 100")
    except Exception as e:
        st.error(f"Error while predicting: {e}")
        st.write("Check if your feature names & order in the DataFrame match the ones used in training.")
