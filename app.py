import streamlit as st

st.set_page_config(page_title="GURU AV PREDICTOR 2.0", layout="centered")

st.markdown("<h1 style='text-align: center; color: red;'>GURU AV PREDICTOR 2.0</h1>", unsafe_allow_html=True)

st.success("Welcome to Guru's Aviator and Lottery Predictor!")

prediction = st.button("Predict Now")

if prediction:
    st.write("Prediction: RED Signal Incoming!")
 import streamlit as st
from rajaluck_data import fetch_data

st.set_page_config(page_title="Guru AV Predictor 2.0", layout="centered")

st.title("GURU AV PREDICTOR 2.0 - Real-Time Prediction")
st.markdown("*Game: Win Go 30s*")

# Data fetch
data = fetch_data.get_win_go_30s_data()

# Show data
st.metric("Predicted Color", data["color"])
st.metric("Round ID", data["round_id"])
st.metric("Timer", data["timer"])
