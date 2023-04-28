import streamlit as st
import pandas as pd
import numpy as np
from df_change import df_change

def danhsach():
  col1, col2, col3, col4 = st.columns(4)
  dfmid = df_change()
  COLS_mid = dfmid.columns.values.tolist().copy()
  needrop = []
  
  with col1:
    st.write('Giới tính')
    unigen = np.unique(dfmid['Gen'])
    check_gender = np.array([st.checkbox(i) for i in unigen])
    A_gender = np.stack((check_gender,unigen,np.array(['Gen']*len(unigen)))).T

  with col2:
    unigrade = np.unique(dfmid['Grade']).tolist()
    grades = np.array(['Tất cả']+ unigrade)
    radio = st.radio(label='Khối lớp', options=grades)
    if radio == 'Tất cả':
      A_grade = np.stack((np.array([True]*len(unigrade)),unigrade,np.array(['Grade']*len(unigrade)))).T
    else:
      unigrade.remove(radio)
      A_grade = np.stack((np.array([False]*len(unigrade)),unigrade,np.array(['Grade']*len(unigrade)))).T
    
  st.write(A_grade)
  dfmid.drop(columns=COLS_mid[17:], inplace=True)
  st.write(dfmid)
    
danhsach()
