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
      a1 = A[A[:,1]==i]
      a = a1[:,0].astype(float)
      B.append(a1[np.argmax(a)])
      B.append(a1[np.argmin(a)])
      A = A.tolist()
    B = np.array(B)
    b = B[:,0].astype(float)

    nhanxet = []
    for i in np.unique(B[:,1]):
      B1 = B[B[:,1]==i]
      b1 = b[B[:,1]==i]
      nhanxet.append('Đối với học sinh '+i+': Lớp '+B1[:,2][0]+' có điểm tổng cao nhất ('+str(np.round(b1[0],1))+' điểm) và lớp '+B1[:,2][1]+' có điểm tổng thấp nhất ('+str(np.round(b1[1],1))+' điểm).')
    
    C = []
    D = []
    for i in np.unique(dfmid['Subject']):
      C.append([dfmid[option][dfmid['Subject']==i].sum(),i])
    C = np.array(C)
    c = C[:,0].astype(float)
    D.append(C[np.argmax(c)])
    D.append(C[np.argmin(c)])
    D = np.array(D)
    d = D[:,0].astype(float)
    nhanxet.append('Khối '+D[:,1][0]+' có điểm tổng cao nhất ('+str(np.round(d[0],1))+' điểm) và khối '+D[:,1][1]+' có điểm tổng thấp nhất ('+str(np.round(d[1],1))+' điểm).')
    
    
  return nhanxet
