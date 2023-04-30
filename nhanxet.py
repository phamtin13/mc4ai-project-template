import streamlit as st
import numpy as np
from df_change import df_change

def nhanxet(option,types):
  dfmid = df_change()
  COLS = dfmid.columns.values.tolist().copy()
  if types == 'Biểu đồ cột (histogram)':
    A = []
    B = []
    for i in np.unique(dfmid['Gen']):
      for j in np.unique(dfmid['PYTHON-CLASS']):
        A.append([dfmid[option][(dfmid['Gen']==i)&(dfmid['PYTHON-CLASS']==j)].sum(),i,j])
      A = np.array(A)
      gen = A[A[:,1]==i]
      a = gen[:,0].astype(float)
      B.append(gen[np.argmax(a)])
      B.append(gen[np.argmin(a)])
      A = A.tolist()
    B = np.array(B)
    c = B[:,0].astype(float)

    nhanxet = []
    for i in np.unique(B[:,1]):
      B1 = B[B[:,1]==i]
      c1 = c[B[:,1]==i]
      nhanxet.append('Đối với học sinh '+i+': Lớp '+B1[:,2][0]+' có điểm tổng cao nhất ('+str(np.round(c1[0],1))+' điểm) và lớp '+B1[:,2][1]+' có điểm tổng thấp nhất ('+str(np.round(c1[1],1))+' điểm).')
    
    C = []
    D = []
    for i in np.unique(dfmid['Subject']):
      C.append([dfmid[option][dfmid['Subject']==i].sum(),i])
      
  return nhanxet
