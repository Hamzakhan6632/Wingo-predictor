python
import streamlit as st
import random

st.set_page_config(page_title="Wingo Predictor", layout="centered")

def get_color(number):
    if number in [1, 3, 7, 9]:
        return "Red"
    elif number in [0, 2, 4, 6, 8]:
        return "Green"
    elif number == 5:
        return "Violet"

st.title("🎯 Wingo AI Color Predictor")
st.markdown("Aakhri 3 numbers daalein:")

n1 = st.number_input("Number 1", 0, 9, step=1)
n2 = st.number_input("Number 2", 0, 9, step=1)
n3 = st.number_input("Number 3", 0, 9, step=1)

if st.button("🔮 Predict"):
    colors = [get_color(n) for n in [n1, n2, n3]]
    prediction = random.choice(["Red", "Green", "Violet"])
    st.success(f"Prediction: {prediction}")
    st.info(f"Pattern: {colors}")
