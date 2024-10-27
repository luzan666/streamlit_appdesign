import streamlit as st
import pandas as pd
from io import StringIO

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

data = """Town,1-Room,2-Room,3-Room,4-Room,5-Room,Executive
ANG MO KIO,NA,"$402,000 ","$612,900 ","$780,000 ",NA,NA
BEDOK,NA,"$390,000 ","$535,000 ","$745,000 ",NA,NA
BISHAN,NA,NA,"$728,000 ","$960,000 ",NA,NA
BUKIT BATOK,"$345,000 ","$390,000 ","$595,000 ","$735,000 ",NA,NA
BUKIT MERAH,NA,NA,"$440,500 ","$885,000 ",NA,NA
BUKIT PANJANG,NA,NA,"$410,000 ","$538,000 ","$650,000 ",NA
BUKIT TIMAH,NA,NA,NA,NA,NA,NA
CENTRAL,NA,NA,"$520,000 ",NA,NA,NA
CHOA CHU KANG,NA,NA,"$390,000 ","$515,000 ","$605,000 ","$773,000 "
CLEMENTI,NA,"$390,000 ","$642,500 ",NA,NA,NA
GEYLANG,NA,"$359,400 ","$877,000 ",NA,NA,NA
HOUGANG,NA,"$430,000 ","$585,000 ","$701,100 ","$900,000 ",NA
JURONG EAST,NA,"$383,000 ","$495,000 ","$632,000 ",NA,NA
JURONG WEST,NA,"$372,500 ","$488,000 ","$600,000 ","$740,500 ",NA
KALLANG/WHAMPOA,NA,"$410,000 ","$860,500 ","$884,000 ",NA,NA
MARINE PARADE,NA,NA,NA,NA,NA,NA
PASIR RIS,NA,NA,"$590,000 ","$695,000 ","$870,000 ",NA
PUNGGOL,NA,"$495,000 ","$622,000 ","$712,500 ",NA,NA
QUEENSTOWN,NA,"$415,500 ","$928,000 ",NA,NA,NA
SEMBAWANG,"$350,000 ","$470,000 ","$567,500 ","$608,000 ","$695,000 ",NA
SENGKANG,NA,"$488,900 ","$600,000 ","$650,000 ","$750,000 ",NA
SERANGOON,NA,"$418,000 ","$600,000 ","$750,000 ",NA,NA
TAMPINES,NA,"$450,000 ","$612,000 ","$728,000 ","$900,000 ",NA
TOA PAYOH,NA,"$385,000 ","$832,500 ","$945,000 ",NA,NA
WOODLANDS,NA,"$425,000 ","$525,000 ","$630,000 ","$855,000 ",NA
YISHUN,"$327,500 ","$408,000 ","$530,000 ","$660,000 ","$835,000 ",NA"""

# Use StringIO to simulate a file-like object
df = pd.read_csv(StringIO(data))

# Select box for the town
town_option = st.selectbox('Which town do you like to live in?', df['Town'])

# Select box for the room type
room_options = ['1-Room', '2-Room', '3-Room', '4-Room', '5-Room', 'Executive']
room_option = st.selectbox('Which flat type do you like to live in?', room_options)

# Retrieve the corresponding price
price = df.loc[df['Town'] == town_option, room_option].values[0]

# Display the result
price


# Create a DataFrame for charting
chart_data = pd.DataFrame({
    'Flat Type': room_options,
    'Price': prices_numeric
})

# Display the bar chart
st.bar_chart(chart_data.set_index('Flat Type'))
