import streamlit as st
import pandas as pd
import numpy as np

def danhsach():
  df = pd.read_csv("py4ai-score.csv", low_memory=False)
  COLS = df.columns.values.tolist().copy()
  col1, col2, col3, col4 = st.columns(4)
  st.title('Hello')
  
  with col1:
    st.write('Giới tính')  
  with col2:
    st.write('Giới tính') 
  with col3:
    st.write('Giới tính')
  with col4:
    st.write('Giới tính') 
