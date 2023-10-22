import streamlit as st

from components.sidebar import sidebar
from components.uploadData import dataTab

st.set_page_config(page_title="MediGuard", page_icon="📖", layout="wide")
st.markdown("<h1 style='text-align: center;'>📖 MediGuard</h1>", unsafe_allow_html=True)

dataTab()
sidebar()

with open("form_submit_state.txt", "r") as file:
    form_submit_state = file.read()
    
if form_submit_state == "pressed":
    #runML()
    pass
    
