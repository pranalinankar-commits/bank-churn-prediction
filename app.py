import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("Bank Customer Churn Prediction")

st.write("Enter Customer Details:")

# Inputs
credit = st.number_input("Credit Score", 300, 900)
age = st.slider("Age", 18, 100)
tenure = st.slider("Tenure", 0, 10)
balance = st.number_input("Balance")
products = st.slider("Number of Products", 1, 4)
active = st.selectbox("Active Member", [0,1])
salary = st.number_input("Estimated Salary")

# Dummy model (for demo)
if st.button("Predict"):
    st.success("Churn Probability: 0.75 (Demo Output)")
