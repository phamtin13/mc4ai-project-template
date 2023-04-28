import streamlit as st
import pandas as pd
import numpy as np
from df_change import df_change

def danhsach():
  df = pd.read_csv("py4ai-score.csv", low_memory=False)
  col1, col2, col3, col4 = st.columns(4)
  dfmid = df_change()
  COLS_mid = dfmid.columns.values.tolist().copy()
  needrop = []
  
  with col1:
    st.write('Giới tính')
    check_gender = np.array([st.checkbox(i) for i in np.unique(dfmid['Gen'])])
    A_gender = np.stack((check_gender,np.unique(dfmid['Gen']),np.array(['Gen']*len(np.unique(dfmid['Gen'])))))
    st.write(A_gender)
  dfmid.drop(columns=COLS_mid[17:], inplace=True)
  st.write(dfmid)
    
danhsach()
