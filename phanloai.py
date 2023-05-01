import streamlit as st
import numpy as np
from df_change import df_change
from sklearn.cluster import KMeans
import plotly.graph_objects as go

def phanloai():
  dfmid = df_change()
  dfmid.rename(columns={'S6' : 'Midterm Exam','S10' : 'Final Exam'}, inplace=True)
  COLS = dfmid.columns.values.tolist().copy()
  COLS.remove('BONUS')
  options = COLS[4:14]
  st.write('Chọn 2 hoặc 3 đặc trưng bạn muốn:')
  check = []
  cols = st.columns(5)
  for i in range(2):
    for j in range(5):
      check.append(str(cols[j].checkbox(options[5*i+j],key=str(options[5*i+j])+' key')))
  A = np.stack((check,options)).T
  st.write(A)
  st.write(A[A[:,0]==True,1])
  
  if len(A[A[:,0]=='True']) == 0:
    st.info('Hãy chọn 2 hoặc 3 đặc trưng mà bạn muốn.')
    
  elif len(A[A[:,0]=='True']) == 1:
    st.info('Bạn đã chọn: '+A[A[:,0]==True,1]+'. Xin hãy chọn 1 hoặc 2 cái nữa.')
    
  elif len(A[A[:,0]=='True']) > 3:
    st.error('Xin lỗi, bạn chỉ được chọn 2 hoặc 3 đặc trưng thôi. Xin hãy chọn lại.')
   
  else:
    st.success('Chào bạn.')
  
  #if option == '3 đặc trưng':
    #X = np.stack((dfmid['Homework'],dfmid['Midterm Exam'],dfmid['Final Exam'])).T
    #kmeans = KMeans(n_clusters=2, n_init='auto')
    #kmeans.fit(X)
    #datas = np.linspace(0, 10, 100)
    #xx, yy = np.meshgrid(datas, datas)
    #xy = np.c_[xx.ravel(), yy.ravel()]
    #z = kmeans.predict(xy)
    #z = z.reshape(xx.shape)
    #st.write(fig = go.Figure(data=[go.Scatter3d(x=X[:,0], y=X[:,1], z=X[:,2], mode='markers'),
                      #go.Surface(x=datas, y=datas, z=z)]))
  
phanloai()
