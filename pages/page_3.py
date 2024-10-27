import streamlit as st
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

st.markdown("# Use_Case 2: CPF Grant Calculator")
st.sidebar.markdown("# Use_Case 2: CPF Grant Calculator")

st.markdown ('# CPF Housing Grant for Resale Flats (Families)')
data_1 = """Household,2-to 4-room,5-room or bigger,
First timer SC-SC couples,"80,000 ","50,000",
First-timer SC-SPR couples,"70,000 ","40,000 ",
First- and second-timer SC-SC couples,"40,000 ","25,000 ","""

# Use StringIO to simulate a file-like object
df_1 = pd.read_csv(StringIO(data_1))

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
data_2 = """Families Income Ceiling,CPF grant amount,
"Not more than $1,500","120,000 ",
"$1,501 to $2,000","110,000 ",
"$2,001 to $2,500","105,000",
"$2,501 to $3,000","95,000 ",
"$3,001 to $3,500","90,000 ",
"$3,501 to $4,000","80,000 ",
"$4,001 to $4,500","70,000 ",
"$4,501 to $5,000","65,000 ",
"$5,001 to $5,500","55,000 ",
"$5,501 to $6,000","50,000 ",
"$6,001 to $6,500","40,000 ",
"$6,501 to $7,000","30,000 ",
"$7,001 to $7,500","25,000 ",
"$7,501 to $8,000","20,000 ",
"$8,001 to $8,500","10,000 ",
"$8,501 to $9,000","5,000 ","""

# Use StringIO to simulate a file-like object
df_2 = pd.read_csv(StringIO(data_2))

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

data_2 = StringIO(data_2)
df = pd.read_csv(data_2, sep='\t')

# Convert the 'CPF grant amount' column to numeric
df['CPF grant amount'] = pd.to_numeric(df['CPF grant amount'])

# Create the histogram
st.title("CPF Grant Amount Histogram")
plt.figure(figsize=(10, 6))
plt.hist(df['CPF grant amount'], bins=10, color='blue', alpha=0.7)
plt.title('Histogram of CPF Grant Amounts')
plt.xlabel('CPF Grant Amount ($)')
plt.ylabel('Frequency')

# Display the histogram in Streamlit
st.pyplot(plt)
