import streamlit as st
import pandas as pd
import numpy as np
from df_change import df_change

def danhsach():
  col1, col2, col3, col4 = st.columns(4)
  dfmid = df_change()
  COLS_mid = dfmid.columns.values.tolist().copy()
  
  with col1:
    st.write('Giới tính')
    unigen = np.unique(dfmid['Gen'])
    check_gender = [str(st.checkbox(i)) for i in unigen]
    A_gender = np.stack((check_gender,unigen,['Gen']*len(unigen))).T

  with col2:
    unigrade = np.unique(dfmid['Grade']).tolist()
    grades = np.array(['Tất cả']+ unigrade)
    radio = st.radio(label='Khối lớp', options=grades)
    if radio == 'Tất cả':
      A_grade = np.stack((['True']*len(unigrade),unigrade,['Grade']*len(unigrade))).T
    else:
      unigrade.remove(radio)
      A_grade = np.stack((['False']*len(unigrade),unigrade,['Grade']*len(unigrade))).T
    
  with col3:
    uniroom = np.unique(dfmid['Classroom']).tolist()
    rooms = np.array(['Tất cả']+ uniroom)
    option = st.selectbox('Phòng',rooms)
    if option == 'Tất cả':
      A_room = np.stack((['True']*len(uniroom),uniroom,['Classroom']*len(uniroom))).T
    else:
      uniroom.remove(option)
      A_room = np.stack((['False']*len(uniroom),uniroom,['Classroom']*len(uniroom))).T
  
  with col4:
    uniday = np.unique(dfmid['Part of day'])[::-1].tolist()
    options = st.multiselect('Buổi', uniday)
    if len(options) != 0 and len(options) != len(uniday):
      for i in options:
        uniday.remove(i)
      A_day = np.stack((['False']*len(uniday),uniday,['Part of day']*len(uniday))).T
    else:
      A_day = np.stack((['True']*len(uniday),uniday,['Part of day']*len(uniday))).T
      
  unisub = np.unique(dfmid['Subject']).tolist()
  unisub.remove('Khác')
  unisub.append('Khác')
  check_sub = []
  cols = st.columns(5)
  for i in range(2):
    for j in range(5):
      check_sub.append(str(cols[j].checkbox(unisub[5*i+j],key=unisub[5*i+j]+'key')))
  A_sub = np.stack((check_sub,unisub,['Subject']*len(unisub))).T

  A = np.concatenate((A_gender, A_grade, A_room, A_day, A_sub))

  needrop = []
  for i in A:
    if i[0] == 'False':
      needrop += np.where(dfmid[str(i[2])]==str(i[1]))[0].tolist()
  
  dfmid.drop(np.unique(needrop), inplace=True)
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
    
danhsach()
