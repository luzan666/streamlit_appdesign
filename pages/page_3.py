import streamlit as st
import pandas as pd

st.markdown("# Use_Case 2: CPF Grant Calculator")
st.sidebar.markdown("# Use_Case 2: CPF Grant Calculator")

st.markdown ('# CPF Housing Grant for Resale Flats (Families)')
# Read the CSV file
df_1 = pd.read_csv ('/workspaces/streamlit_appdesign/pages/CPF grant.csv')
# Select box from df_1 > household 
household = st.selectbox('Household Type:', df_1['Household'])
# Select box from df_1 > flat type 
flat_options = ['2-to 4-room', '5-room or bigger']
flattype = st.selectbox('Flat Type:', flat_options)
# Retrieve the base grant 
grant_1 = df_1.loc[df_1['Household'] == household, flattype].values[0]
# Clean and convert grant_1 to numeric
try:
    grant_1 = pd.to_numeric(grant_1.replace(',', '').strip())
except ValueError:
    grant_1 = 0  # Default to 0 or handle as needed
# Display the result
st.write('Grant Amount ($):', grant_1)


st.markdown ('# Enhanced CPF Housing Grant (Families)')
#Read the CSV file 
df_2 = pd.read_csv ('/workspaces/streamlit_appdesign/pages/EHG.csv')
# Select box from df_2 > income
Income_ceiling = st.selectbox('Families Income Ceiling:', df_2['Families Income Ceiling'])
# Retrieve the enhance grant 
grant_2 = df_2.loc[df_2['Families Income Ceiling'] == Income_ceiling, 'CPF grant amount'].values[0]
# Clean and convert grant_2 to numeric
try:
    grant_2 = pd.to_numeric(grant_2.replace(',', '').strip())
except ValueError:
    grant_2 = 0  # Default to 0 or handle as needed
# Display the result
st.write('Grant Amount($):' ,grant_2)

Total_grant = grant_1 + grant_2 

st.write('Total Grant Amount ($):', Total_grant)