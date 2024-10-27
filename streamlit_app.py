import streamlit as st
import numpy as np
import pandas as pd 

st.title("Buying HDB flat in the resale market")
st.sidebar.markdown ("# Main page")

with st.expander("IMPORTANT NOTICE"):
    st.write("""
This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.
Always consult with qualified professionals for accurate and personalized advice.
    """)
# Define the password
PASSWORD = "1234"

# Create a password input field
password = st.text_input("Enter Password:", type="password")

# Check if the password is correct
if password == PASSWORD:
    st.title("Protected Streamlit App")
    st.write("Welcome to the app!")
    
    # Add your app content here
    # Example: Display a table, charts, etc.
    

