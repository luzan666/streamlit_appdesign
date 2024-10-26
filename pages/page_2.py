import streamlit as st
import pandas as pd

st.markdown("# Use_Case 1: Intelligent Search")
st.sidebar.markdown("# Use_Case 1: Intelligent Search")

st.markdown ('''
The statistics provide the median prices for reslae transactions of a particular flay type in a given town.
This is based on resale cases registered in the quarter. The median price (at fiftieth percentile) tells 
you that half of the flats transcted during the quarter were sold above the median price and half were 
sold below the median price. The median resale prices are inclusive of Cash-Over-Valuation (COV) for 
transactions where resale prices are above marrket valuations. ''') 

st.markdown ('''For 'nan'result, there are either no resale transactions in the quarter or fewer than 20 resale transations 
for a particular town and flat type. The median prices for these cases are not displayed, as they may not be 
representative.''')

# Read the CSV file
df = pd.read_csv('/workspaces/streamlit_appdesign/pages/hdb_price.csv')

# Select box for the town
town_option = st.selectbox('Which town do you like to live in?', df['Town'])

# Select box for the room type
room_options = ['1-Room', '2-Room', '3-Room', '4-Room', '5-Room', 'Executive']
room_option = st.selectbox('Which flat type do you like to live in?', room_options)

# Retrieve the corresponding price
price = df.loc[df['Town'] == town_option, room_option].values[0]

# Display the result
price