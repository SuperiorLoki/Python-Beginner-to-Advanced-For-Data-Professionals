import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/"

def report():
    response = requests.get(f"{API_URL}/report/")
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []

    st.header("Full Expenses List")
    df = pd.DataFrame(existing_expenses)
    st.write(df)