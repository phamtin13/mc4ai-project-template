import pandas as pd
import streamlit as st
def danhsach():
  df = pd.read_csv("py4ai-score.csv", low_memory=False)
  COLS = df.columns.values.tolist().copy()
  check = st.checkbox('Boy')
  radio = st.radio('Radio', ('Option 1', 'Option 2', 'Option 3'), horizontal=True)
  if st.button('OK'):
    st.write('Check box:', check)
    st.write('Radio:', radio, type(radio))
danhsach()
