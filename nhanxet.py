import numpy as np
import re
from df_change import df_change

def to_data(A,A_data):
  if len(A) == 1:
    A_data.append(A[0].tolist())
  else:
    to_choose = ' / '.join(A[:,2])
    A_data.append([A[0][0],A[0][1],to_choose])

def nhanxet(option,choose,sub,good,bad):
  dfmid = df_change()
  if sub == 'PYTHON-CLASS':
    A = []
    A_data = []
    nhanxet = []
    for i in np.unique(dfmid['Gen']):
      for j in np.unique(dfmid['PYTHON-CLASS']):
        A.append([choose(dfmid[option][(dfmid['Gen']==i)&(dfmid['PYTHON-CLASS']==j)]),i,j])
      A = np.array(A)
      A_new = A[A[:,1]==i]
      A_numnew = A_new[:,0].astype(float)  
      A_max = max(A_numnew)
      A_huge = A_new[A_numnew == A_max]
      A_min = min(A_numnew)
      A_small = A_new[A_numnew == A_min]
      to_data(A_huge,A_data)
      to_data(A_small,A_data)
      A_data = np.array(A_data)
      Ada = A_data[A_data[:,1]==i]
      nhanxet.append('Đối với học sinh '+Ada[0][1]+', lớp '+Ada[0][2]+good+str(np.round(float(Ada[0][0]),1))+' điểm, còn lớp '+Ada[1][2]+bad+str(np.round(float(Ada[1][0]),1))+' điểm.')
      A = A.tolist()
      A_data = A_data.tolist()
  else:
    A = []
    A_data = []
    nhanxet = []
    for i in np.unique(dfmid['Subject']):
      A.append([choose(dfmid[option][dfmid['Subject']==i]),i,i])
    A = np.array(A)
    A_numnew = A[:,0].astype(float)  
    A_max = max(A_numnew)
    A_huge = A[A_numnew == A_max]
    A_min = min(A_numnew)
    A_small = A[A_numnew == A_min]
    to_data(A_huge,A_data)
    to_data(A_small,A_data)
    nhanxet.append('Học sinh khối '+A_data[0][2]+good+str(np.round(float(A_data[0][0]),1))+' điểm, còn khối '+A_data[1][2]+bad+str(np.round(float(A_data[1][0]),1))+' điểm.')
  return '  \n'.join(nhanxet)
