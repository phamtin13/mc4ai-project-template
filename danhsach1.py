import streamlit as st
import pandas as pd
import numpy as np
from df_change import df_change

def danhsach1():
  col1, col2, col3, col4 = st.columns(4)
  dfmid = df_change()
  COLS_mid = dfmid.columns.values.tolist().copy()
  
  with col1:
    st.write('Giới tính')
    unigen = np.unique(dfmid['Gen'])
    check_gender = [str(st.checkbox(i)) for i in unigen]
    A_gender = np.stack((check_gender,unigen)).T
    for i in A_gender:
      if i[0] == True:
        dfmid = dfmid.iloc[dfmid['Gen']==i[1]]

  with col2:
    unigrade = np.unique(dfmid['Grade']).tolist()
    grades = np.array(['Tất cả']+ unigrade)
    radio = st.radio(label='Khối lớp', options=grades)
    if radio != 'Tất cả':
      dfmid = dfmid.loc[dfmid['Grade']==radio]
    
  with col3:
    uniroom = np.unique(dfmid['Classroom']).tolist()
    rooms = np.array(['Tất cả']+ uniroom)
    option = st.selectbox('Phòng',rooms)
    if option != 'Tất cả':
      dfmid = dfmid.loc[dfmid['Classroom']==option]
  
  with col4:
    uniday = np.unique(dfmid['Part of day'])[::-1].tolist()
    options = st.multiselect('Buổi', uniday)
    if len(options) != 0 and len(options) != len(uniday):
      if len(options) == 1:
        dfmid = dfmid.loc[dfmid['Part of day']==options]
      else:
        for i in options:
          dfmid = dfmid.loc[dfmid['Part of day']==i]
      
  unisub = np.unique(dfmid['Subject']).tolist()
  unisub.remove('Khác')
  unisub.append('Khác')
  check_sub = []
  cols = st.columns(5)
  for i in range(2):
    for j in range(5):
      check_sub.append(str(cols[j].checkbox(unisub[5*i+j],key=unisub[5*i+j]+'key')))
  A_sub = np.stack((check_sub,unisub)).T
  for i in A_sub:
      if i[0] == True:
        dfmid = dfmid.loc[dfmid['Subject']==i[1]]
  
  st.write('Số học sinh:',len(dfmid),'('+str(len(dfmid[dfmid['Gen']=='Nam']))+' nam, '+str(len(dfmid[dfmid['Gen']=='Nữ']))+' nữ)')
  st.write('GPA: cao nhất',dfmid['GPA'].max(),', thấp nhất',dfmid['GPA'].max(),', trung bình',np.round(dfmid['GPA'].mean(),1))
  mgai = len(dfmid[dfmid['REG-MC4AI']=='Y'])
  st.write('Số học sinh đăng kí khoá MC4AI:',mgai)
  if len(dfmid) == 0:
    r = 0
  else:
    r = np.round((mgai/len(dfmid))*100,1)
  st.write('Phần trăm số học sinh đăng kí khoá MC4AI:',r,'%')
  dfmid.drop(columns=COLS_mid[17:], inplace=True)
  
  st.write(dfmid)
    
danhsach1()
