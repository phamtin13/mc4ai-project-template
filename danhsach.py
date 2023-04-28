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
    A_gender = np.stack((check_gender,unigen,['Gen']*len(unigen))).T

  with col2:
    unigrade = np.unique(dfmid['Grade']).tolist()
    grades = np.array(['Tất cả']+ unigrade)
    radio = st.radio(label='Khối lớp', options=grades)
    if radio == 'Tất cả':
      A_grade = np.stack(([True]*len(unigrade),unigrade,['Grade']*len(unigrade))).T
    else:
      unigrade.remove(radio)
      A_grade = np.stack(([False]*len(unigrade),unigrade,['Grade']*len(unigrade))).T
    
  with col3:
    uniroom = np.unique(dfmid['Classroom']).tolist()
    rooms = np.array(['Tất cả']+ uniroom)
    option = st.selectbox('Phòng',rooms)
    if option == 'Tất cả':
      A_room = np.stack(([True]*len(uniroom),uniroom,['Classroom']*len(uniroom))).T
    else:
      uniroom.remove(option)
      A_room = np.stack(([False]*len(uniroom),uniroom,['Classroom']*len(uniroom))).T
  
  with col4:
    uniday = np.unique(dfmid['Part of day']).tolist()
    options = st.multiselect('Buổi', uniday)
    if len(options) != 0:
      for i in options:
        uniday.remove(i)
      A_day = np.stack(([False]*len(uniday),uniday,['Part of day']*len(uniday))).T
    else:
      A_day = np.stack(([True]*len(uniday),uniday,['Part of day']*len(uniday))).T
  st.write(A_day)
  dfmid.drop(columns=COLS_mid[17:], inplace=True)
  st.write(dfmid)
    
danhsach()
