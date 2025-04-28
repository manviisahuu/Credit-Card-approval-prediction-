# save this as app.py
'''import streamlit as st
import pandas as pd

# Set page title
st.title('Credit Card Approval Prediction')

st.write('Please enter the following details:')

# Take user inputs
amt_income_total = st.number_input('Total Annual Income (in ₹)', min_value=0, step=1000)
age = st.number_input('Age (in years)', min_value=0, step=1)
cnt_children = st.number_input('Number of Children', min_value=0, step=1)

# Submit button
if st.button('Check Approval'):

    # Create default dictionary for all 47 columns
    data = {
        'code_gender': 0,
        'flag_own_car': 0,
        'flag_own_realty': 0,
        'cnt_children': cnt_children,
        'days_employed': 0,
        'flag_work_phone': 0,
        'flag_phone': 0,
        'flag_email': 0,
        'cnt_fam_members': 1,
        'age': age,
        'approved': 0,  # will calculate below
        'amt_income_total_log': 0,  # we can ignore log here
        'name_income_type_Pensioner': 0,
        'name_income_type_State servant': 0,
        'name_income_type_Student': 0,
        'name_income_type_Working': 1,
        'name_education_type_Higher education': 0,
        'name_education_type_Incomplete higher': 0,
        'name_education_type_Lower secondary': 0,
        'name_education_type_Secondary / secondary special': 1,
        'name_family_status_Married': 0,
        'name_family_status_Separated': 0,
        'name_family_status_Single / not married': 1,
        'name_family_status_Widow': 0,
        'name_housing_type_House / apartment': 1,
        'name_housing_type_Municipal apartment': 0,
        'name_housing_type_Office apartment': 0,
        'name_housing_type_Rented apartment': 0,
        'name_housing_type_With parents': 0,
        'occupation_type_Cleaning staff': 0,
        'occupation_type_Cooking staff': 0,
        'occupation_type_Core staff': 0,
        'occupation_type_Drivers': 0,
        'occupation_type_HR staff': 0,
        'occupation_type_High skill tech staff': 0,
        'occupation_type_IT staff': 0,
        'occupation_type_Laborers': 0,
        'occupation_type_Low-skill Laborers': 0,
        'occupation_type_Managers': 0,
        'occupation_type_Medicine staff': 0,
        'occupation_type_Private service staff': 0,
        'occupation_type_Realty agents': 0,
        'occupation_type_Sales staff': 0,
        'occupation_type_Secretaries': 0,
        'occupation_type_Security staff': 0,
        'occupation_type_Unknown': 1,
        'occupation_type_Waiters/barmen staff': 0
    }

    # Create a dataframe
    df = pd.DataFrame([data])

    # Apply your approval formula
    approved = (
        (amt_income_total > 150000) &
        (age < 60) &
        (cnt_children <= 2)
    )

    # Show result
    if approved:
        st.success('✅ Congratulations! Your Credit Card Application is likely to be Approved.')
    else:
        st.error('❌ Sorry! Your Credit Card Application is likely to be Rejected.')

'''
import streamlit as st
import pandas as pd
import random
from streamlit.components.v1 import html

# Set page title
st.title('Credit Card Approval Prediction')

# Sidebar with basic instructions on how to get approved
with st.sidebar:
    st.header("How to Get Approved?")
    st.write("""
        - **Gender:** Male/Female
        - **Annual Income:** Higher income increases chances
        - **Education:** Higher education or higher secondary
        - **Children:** Fewer children are better
        - **Marital Status:** Single/Not married preferred
        - **Family Members:** Fewer family members are better
        - **Age:** Below 60 years preferred
        """)

# Take user inputs
gender = st.selectbox('Gender', ['Male', 'Female'])
amt_income_total = st.number_input('Total Annual Income (in ₹)', min_value=0, step=1000)
education = st.selectbox('Education Level', ['Higher education', 'Incomplete higher', 'Lower secondary', 'Secondary / secondary special'])
cnt_children = st.number_input('Number of Children', min_value=0, step=1)
marital_status = st.selectbox('Marital Status', ['Married', 'Single / not married', 'Widow', 'Separated'])
cnt_fam_members = st.number_input('Number of Family Members', min_value=1, step=1)
age = st.number_input('Age (in years)', min_value=18, step=1)

# Submit button
if st.button('🔮 Predict'):

    # Create default dictionary for all 47 columns with the new inputs
    data = {
        'code_gender': 1 if gender == 'Male' else 0,
        'flag_own_car': 0,
        'flag_own_realty': 0,
        'cnt_children': cnt_children,
        'days_employed': 0,
        'flag_work_phone': 0,
        'flag_phone': 0,
        'flag_email': 0,
        'cnt_fam_members': cnt_fam_members,
        'age': age,
        'approved': 0,  # will calculate below
        'amt_income_total_log': amt_income_total,  # we can use raw income here
        'name_income_type_Pensioner': 0,
        'name_income_type_State servant': 0,
        'name_income_type_Student': 0,
        'name_income_type_Working': 1,
        'name_education_type_Higher education': 1 if education == 'Higher education' else 0,
        'name_education_type_Incomplete higher': 1 if education == 'Incomplete higher' else 0,
        'name_education_type_Lower secondary': 1 if education == 'Lower secondary' else 0,
        'name_education_type_Secondary / secondary special': 1 if education == 'Secondary / secondary special' else 0,
        'name_family_status_Married': 1 if marital_status == 'Married' else 0,
        'name_family_status_Separated': 1 if marital_status == 'Separated' else 0,
        'name_family_status_Single / not married': 1 if marital_status == 'Single / not married' else 0,
        'name_family_status_Widow': 1 if marital_status == 'Widow' else 0,
        'name_housing_type_House / apartment': 1,
        'name_housing_type_Municipal apartment': 0,
        'name_housing_type_Office apartment': 0,
        'name_housing_type_Rented apartment': 0,
        'name_housing_type_With parents': 0,
        'occupation_type_Cleaning staff': 0,
        'occupation_type_Cooking staff': 0,
        'occupation_type_Core staff': 0,
        'occupation_type_Drivers': 0,
        'occupation_type_HR staff': 0,
        'occupation_type_High skill tech staff': 0,
        'occupation_type_IT staff': 0,
        'occupation_type_Laborers': 0,
        'occupation_type_Low-skill Laborers': 0,
        'occupation_type_Managers': 0,
        'occupation_type_Medicine staff': 0,
        'occupation_type_Private service staff': 0,
        'occupation_type_Realty agents': 0,
        'occupation_type_Sales staff': 0,
        'occupation_type_Secretaries': 0,
        'occupation_type_Security staff': 0,
        'occupation_type_Unknown': 1,
        'occupation_type_Waiters/barmen staff': 0
    }

    # Create a dataframe
    df = pd.DataFrame([data])

    # Apply your approval formula
    approved = (
        (amt_income_total > 300000) &
        (25 < age < 60) &
        (cnt_children <= 2)
    )

    if approved:
        st.success('✅ Congratulations! Your Credit Card Application is likely to be Approved.')
        st.balloons()  # Confetti Effect
    else:
        st.error('❌ Sorry! Your Credit Card Application is likely to be Rejected.')
    