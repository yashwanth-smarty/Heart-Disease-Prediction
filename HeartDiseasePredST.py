import pickle
import numpy as np
import streamlit as st

# Load the model
loaded_model = pickle.load(open('heartdiseasepred.sav', 'rb'))

# Prediction function
def pred_function(input_data):
    tc = np.asarray(input_data, dtype=np.float64)  # Ensure the data is in numeric form
    abc = tc.reshape(1, -1)
    res = loaded_model.predict(abc)
    if res[0] == 0:
        return 'The person has a Healthy Heart'
    else:
        return 'The person\'s Heart is not Healthy'

# Main function
def main():
    st.title('Heart Disease Prediction System')

    # Input fields
    age = st.number_input('Enter age', min_value=0, max_value=120, value=25)
    sex = st.selectbox('Select gender', options=[0, 1], index=0)
    cp = st.number_input('Enter cp', min_value=0, max_value=4, value=0)
    trestbps = st.number_input('Enter trestbps', min_value=0, value=120)
    chol = st.number_input('Enter chol', min_value=0, value=200)
    fbs = st.selectbox('Enter fbs', options=[0, 1], index=0)
    restecg = st.number_input('Enter restecg', min_value=0, max_value=2, value=0)
    thalach = st.number_input('Enter thalach', min_value=0, value=150)
    exang = st.selectbox('Enter exang', options=[0, 1], index=0)
    oldpeak = st.number_input('Enter oldpeak', min_value=0.0, value=1.0)
    slope = st.number_input('Enter slope', min_value=0, max_value=2, value=0)
    ca = st.number_input('Enter ca', min_value=0, max_value=4, value=0)
    thal = st.number_input('Enter thal')

    result = ''

    # Get the result
    if st.button('Get Result'):
        result = pred_function([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])

    st.success(result)

if __name__ == '__main__':
    main()
