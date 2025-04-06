import streamlit as st

st.set_page_config(page_title="GURU AV PREDICTOR 2.0", layout="centered")

st.markdown("<h1 style='text-align: center; color: red;'>GURU AV PREDICTOR 2.0</h1>", unsafe_allow_html=True)

st.success("Welcome to Guru's Aviator and Lottery Predictor!")

prediction = st.button("Predict Now")

if prediction:
    st.write("Prediction: RED Signal Incoming!")
