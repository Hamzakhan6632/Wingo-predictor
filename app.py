
import streamlit as st
import random
n1 = st.number_input("Number 1", 0, 9, step=1)
‎n2 = st.number_input("Number 2", 0, 9, step=1)
‎n3 = st.number_input("Number 3", 0, 9, step=1)
‎
‎if 'history' not in st.session_state:
‎    st.session_state.history = []
‎
‎if st.button("🔮 Predict"):
‎    colors = [get_color(n) for n in [n1, n2, n3]]
‎    prediction = random.choice(["Red", "Green", "Violet"])
‎    st.session_state.history.append((colors, prediction))
‎
‎    st.success(f"Prediction: {prediction}")
‎    st.info(f"Pattern: {colors}")
‎
‎Show previous results
‎if st.session_state.history:
‎    st.subheader("📜 Previous Predictions:")
‎    for idx, (pattern, result) in enumerate(reversed(st.session_state.history[-5:]), 1):
‎        st.write(f"{idx}. Pattern: {pattern} → Prediction: {result}")
