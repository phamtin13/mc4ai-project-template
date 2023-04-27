import streamlit as st
import pandas as pd
import numpy as np
from df_change import df_change

def danhsach():
  df = pd.read_csv("py4ai-score.csv", low_memory=False)
  COLS = df.columns.values.tolist().copy()
  col1, col2, col3, col4 = st.columns(4)
  dfmid = df_change()
  with col1:
    st.write('Giới tính')
 
  st.write(dfmid)
  df.drop(columns=COLS[17:], inplace=True)
    
danhsach()
