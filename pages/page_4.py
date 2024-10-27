import streamlit as st

st.markdown("# Methodology")
st.sidebar.markdown("# Methodology")

st.markdown ("""
dataflow chart 1: 
[Start]
   |
   v
[Display Title and Description]
   |
   v
[Load Data]
   |
   |---> [File Format: CSV]
   |
   v
[User Input Section]
   |-----------------------|
   |                       |
   v                       v
[Select Town]        [Select Room Type]
   |                       |
   v                       v
[Process User Input with LLM]
   |
   v
[API Interaction (Optional)]
   |
   v
[Retrieve Price from DataFrame]
   |
   v
[Display Result]
   |
   v
[Handle Edge Cases]
   |
   v
[End]

             
dataflow chart 2:

 """)
