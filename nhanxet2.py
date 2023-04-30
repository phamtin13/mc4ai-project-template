import streamlit as st
import numpy as np
from df_change import df_change

def median(x):
  unique, counts = np.unique(x, return_counts=True)
  A = np.asarray((unique, counts)).T
  return A[np.argmax(A[:,1]),0]

def nhanxet2(option,types):
  dfmid = df_change()
  COLS = dfmid.columns.values.tolist().copy()
  
  TS = np.array([['Biểu đồ cột (histogram)',np.unique(dfmid['Gen']),np.unique(dfmid['PYTHON-CLASS']),sum],
        ['Biểu đồ cột (histogram)',np.unique(dfmid['Gen']),np.unique(dfmid['PYTHON-CLASS']),sum],
        ['Biểu đồ cột (histogram)',range(len[1]),np.unique(dfmid['Subject']),sum],
        ['Biểu đồ hộp (box)',np.unique(dfmid['Gen']),np.unique(dfmid['PYTHON-CLASS']),median],
        ['Biểu đồ hộp (box)',np.unique(dfmid['Gen']),np.unique(dfmid['PYTHON-CLASS']),median],
        ['Biểu đồ hộp (box)',range(len[1]),np.unique(dfmid['Subject']),median]])
  
  for i in TS:
    if types == i[0]:
      A = []
      B = []
      for x in i[1]:
        for y in i[2]:
          A.append(i[3]([dfmid[option][(dfmid['Gen']==x)&(dfmid['PYTHON-CLASS']==y)]),x,y])
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
    
