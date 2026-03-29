import streamlit as st

st.title("Bank Customer Churn Prediction")

age = st.slider("Age", 18, 100)
balance = st.number_input("Balance")
products = st.slider("Products", 1, 4)

st.write("Prediction coming soon...")
