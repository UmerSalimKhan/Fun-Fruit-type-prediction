import streamlit as st
import joblib

# Load the trained model
model = joblib.load('fruit_classifier_model.joblib')

# Set the title of the app
st.title('🍏 Fruit Classification App 🍊')

# Create a sidebar for user inputs
st.sidebar.header('Input Features')

# Input features from user using sliders
mass = st.sidebar.slider('Mass (g)', min_value=76, max_value=362, value=163, step=1)
width = st.sidebar.slider('Width (cm)', min_value=5.8, max_value=9.6, value=7.1, step=0.1)
height = st.sidebar.slider('Height (cm)', min_value=4.0, max_value=10.5, value=7.7, step=0.1)
color_score = st.sidebar.slider('Color Score', min_value=0.55, max_value=0.93, value=0.76, step=0.01)

# Predict button
if st.sidebar.button('Predict'):
    input_data = [[mass, width, height, color_score]]
    prediction = model.predict(input_data)
    
    # Display the prediction result
    st.write(f'### The predicted fruit label is: **{prediction[0]}**')
    
    # Optionally display a message based on the prediction
    fruit_names = {1: 'Apple', 2: 'Mandarin', 3: 'Orange', 4: 'Lemon'}
    st.write(f'### Fruit Name: **{fruit_names.get(prediction[0], "Unknown")}**')
