# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:30:14 2023

@author: k.DWARAKADEESH
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/k.DWARAKADEESH/OneDrive/Desktop/MULTIPLE DISEASE PREDICTION/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/k.DWARAKADEESH/OneDrive/Desktop/MULTIPLE DISEASE PREDICTION/saved models/heart_model.sav','rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        age = float(age) if age else 0.0

    with col2:
        sex = st.text_input('Sex (0 for female, 1 for male)')
        sex = int(sex) if sex else 0

    with col3:
        cp = st.text_input('Chest Pain types (0-3)')
        cp = int(cp) if cp else 0

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
        trestbps = float(trestbps) if trestbps else 0.0

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        chol = float(chol) if chol else 0.0

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (0 for No, 1 for Yes)')
        fbs = int(fbs) if fbs else 0

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0-2)')
        restecg = int(restecg) if restecg else 0

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved (bpm)')
        thalach = float(thalach) if thalach else 0.0

    with col3:
        exang = st.text_input('Exercise Induced Angina (0 for No, 1 for Yes)')
        exang = int(exang) if exang else 0

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        oldpeak = float(oldpeak) if oldpeak else 0.0

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')
        slope = int(slope) if slope else 0

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0-3)')
        ca = int(ca) if ca else 0

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect (0-2)')
        thal = int(thal) if thal else 0

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        if (
            age > 0 and 0 <= sex <= 1 and 0 <= cp <= 3 and
            trestbps > 0 and chol > 0 and 0 <= fbs <= 1 and
            0 <= restecg <= 2 and thalach > 0 and 0 <= exang <= 1 and
            oldpeak > 0 and 0 <= slope <= 2 and 0 <= ca <= 3 and 0 <= thal <= 2
        ):
            # Assuming heart_disease_model is correctly loaded and trained
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        else:
            heart_diagnosis = 'Please provide valid inputs.'

    st.success(heart_diagnosis)





    
    
        
    
   
    
    
    
    
   