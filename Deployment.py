import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="💓"
)

def load_model():
    with open('heart_disease_model.pickle', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

def show_predict():
    st.title('💓 Heart Disease Prediction')

    with st.form("user_input"):
        st.info('📢 Input data will be generated randomly if not filled. Refresh the page to generate new random input data.')

        rand_age = np.random.randint(27, 77)
        age = st.select_slider('Age', options=[i for i in range(1, 111)], value=rand_age)

        rand_sex = np.random.randint(0, 2)
        sex = st.selectbox('Sex', ("Male", "Female"), index=rand_sex)
        if sex == 'Male':
            sex = 1
        elif sex == 'Female':
            sex = 2

        rand_chestpain = np.random.randint(0, 4)
        chestpain = st.selectbox('Chest Pain Type', ("Asymptomatic", "Non-anginal Pain", "Atypical Angina", "Typical Angina"), index=rand_chestpain)
        if chestpain == 'Asymptomatic':
            chestpain = 1
        elif chestpain == 'Non-anginal Pain':
            chestpain = 2
        elif chestpain == 'Atypical Angina':
            chestpain = 3
        elif chestpain == 'Typical Angina':
            chestpain = 4
        
        rand_restingbp = np.random.randint(60, 201)
        restingbp = st.select_slider('Resting Blood Pressure', options=[i for i in range(60, 201)], value=rand_restingbp)

        rand_cholesterol = np.random.randint(120, 481)
        cholesterol = st.select_slider('Cholesterol', options=[i for i in range(120, 481)], value=rand_cholesterol)

        rand_fastingbs = np.random.randint(0, 2)
        fastingbs = st.selectbox('Fasting Blood Sugar', ("Lower than 120mg/ml", "Greater than 120mg/ml"), index=rand_fastingbs)
        if fastingbs == 'Lower than 120mg/ml':
            fastingbs = 0
        elif fastingbs == 'Greater than 120mg/ml':
            fastingbs = 1

        rand_restingecg = np.random.randint(0, 3)
        restingecg = st.selectbox('Resting Electrocardiographic Results', ("Normal", "Showing probable or definite left ventricular hypertrophy", "Having ST-T wave abnormality"), index=rand_restingecg)
        if restingecg == 'Normal':
            restingecg = 0
        elif restingecg == 'Showing probable or definite left ventricular hypertrophy':
            restingecg = 1
        elif restingecg == 'Having ST-T wave abnormality':
            restingecg = 2

        rand_maxhr = np.random.randint(60, 201)
        maxhr = st.select_slider('Maximum Heart Rate Achieved', options=[i for i in range(60, 201)], value=rand_maxhr)

        rand_exerciseangina = np.random.randint(0, 2)
        exerciseangina = st.selectbox('Exercise Induced Angina', ("Yes", "No"), index=rand_exerciseangina)
        if exerciseangina == 'Yes':
            exerciseangina = 1
        elif exerciseangina == 'No':
            exerciseangina = 0

        rand_oldpeak = np.random.randint(0, 7)
        oldpeak = st.select_slider('Oldpeak (ST Depression Induced by Exercise Relative to Rest)', options=[i for i in range(0, 7)], value=rand_oldpeak)

        rand_st_slope = np.random.randint(0, 3)
        st_slope = st.selectbox('ST Slope', ("Upsloping", "Flat", "Downsloping"), index=rand_st_slope)
        if st_slope == 'Upsloping':
            st_slope = 1
        elif st_slope == 'Flat':
            st_slope = 2
        elif st_slope == 'Downsloping':
            st_slope = 3

        ok = st.form_submit_button("Predict")
        if ok:
            X = np.array([[age, sex, chestpain, restingbp, cholesterol, fastingbs, restingecg, maxhr, exerciseangina, oldpeak, st_slope]])
            pred = model.predict(X)
            if pred == 0:
                st.subheader(f'You do not have a heart disease')
            if pred == 1:
                st.subheader(f'You have a heart disease')

show_predict()