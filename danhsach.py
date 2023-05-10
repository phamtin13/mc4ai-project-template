import streamlit as st
import pandas as pd
import numpy as np
from df_change import df_change

def danhsach():
  col1, col2, col3, col4 = st.columns(4)
  dfmid = df_change()
  COLS_mid = dfmid.columns.values.tolist().copy()
  
  with col1:
    st.write('Giới tính:')
    unigen = np.unique(dfmid['Gen'])
    check_gender = [str(st.checkbox(i,value=True,key=i+' key')) for i in unigen]
    A_gender = np.stack((check_gender,unigen,['Gen']*len(unigen))).T

  with col2:
    unigrade = np.unique(dfmid['Grade']).tolist()
    grades = np.array(['Tất cả']+ unigrade)
    radio = st.radio(label='Khối lớp:', options=grades)
    if radio == 'Tất cả':
      A_grade = np.stack((['True']*len(unigrade),unigrade,['Grade']*len(unigrade))).T
    else:
      unigrade.remove(radio)
      A_grade = np.stack((['False']*len(unigrade),unigrade,['Grade']*len(unigrade))).T
    
  with col3:
    unista = np.unique(dfmid['Status']).tolist()
    stas = np.array(['Tất cả']+ unista)
    option = st.selectbox('Tình trạng học:',stas)
    if option == 'Tất cả':
      A_sta = np.stack((['True']*len(unista),unista,['Status']*len(unista))).T
    else:
      unista.remove(option)
      A_sta = np.stack((['False']*len(unista),unista,['Status']*len(unista))).T
  
  with col4:
    uniroom = np.unique(dfmid['Classroom']).tolist()
    options = st.multiselect('Phòng học và buổi học:', uniroom, default = uniroom)
    if len(options) != 0 and len(options) != len(uniroom):
      difroom = list(set(uniroom) - set(options))
      A_room = np.stack((['False']*len(difroom),difroom,['Classroom']*len(difroom))).T
    elif len(options) == len(uniroom):
      A_room = np.stack((['True']*len(uniroom),uniroom,['Classroom']*len(uniroom))).T
    else:
      A_room = np.stack((['False']*len(uniroom),uniroom,['Classroom']*len(uniroom))).T
  
  st.write('Môn học chính khoá:')
  unisub = np.unique(dfmid['Subject']).tolist()
  unisub.remove('Khác')
  unisub.append('Khác')
  check_sub = []
  cols = st.columns(5)
  for i in range(2):
    for j in range(5):
      check_sub.append(str(cols[j].checkbox(unisub[5*i+j],value=True,key=str(unisub[5*i+j])+' key')))
  A_sub = np.stack((check_sub,unisub,['Subject']*len(unisub))).T

  A = np.concatenate((A_gender, A_grade, A_sta, A_room, A_sub))

  needrop = []
  for i in A:
    if i[0] == 'False':
      needrop += np.where(dfmid[str(i[2])]==str(i[1]))[0].tolist()
  
  dfmid.drop(np.unique(needrop), inplace=True)
  st.write('Số học sinh:',len(dfmid),'('+str(len(dfmid[dfmid['Gen']=='Nam']))+' nam, '+str(len(dfmid[dfmid['Gen']=='Nữ']))+' nữ)')
  st.write('GPA: cao nhất',dfmid['GPA'].max(),', thấp nhất',dfmid['GPA'].min(),', trung bình',np.round(dfmid['GPA'].mean(),1))
  pyai = len(dfmid[dfmid['Fail or Pass']=='Đậu'])
  mgai = len(dfmid[dfmid['REG-MC4AI']=='Y'])
  st.write('Số học sinh đậu khoá PY4AI (GPA tối thiểu phải là 6.0 điểm):',pyai)
  st.write('Số học sinh đăng kí khoá MC4AI:',mgai)
  if len(dfmid) == 0:
    r = 0
    s = 0
  else:
    r = np.round((pyai/len(dfmid))*100,1)
    s = np.round((mgai/len(dfmid))*100,1)

  st.write('Phần trăm số học sinh đậu khoá PY4AI:',r,'%')
  st.write('Phần trăm số học sinh đăng kí khoá MC4AI:',s,'%')

  dfmid.drop(columns=COLS_mid[17:], inplace=True)
  
  st.write(dfmid)
    
danhsach()
