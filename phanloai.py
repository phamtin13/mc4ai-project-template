import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from df_change import df_change
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
import plotly.graph_objects as go

def phanloai():
  dfmid = df_change()
  dfmid.rename(columns={'Homework': 'Điểm bài tập trung bình','S6' : 'Midterm Exam','S10' : 'Final Exam'}, inplace=True)
  COLS = dfmid.columns.values.tolist().copy()
  COLS.remove('BONUS')
  options = np.array(['Điểm bài tập trung bình','Midterm Exam','Final Exam'])
  st.write('Chọn 2 hoặc 3 đặc trưng bạn muốn:')
  check = []
  cols = st.columns(3)
  for i in range(3):
    check.append(str(cols[i].checkbox(options[i],key=str(options[i])+' key')))
  A = np.stack((check,options)).T
  X = np.array(dfmid[A[A[:,0]=='True',1]])
  y = np.array(dfmid['Fail or Pass'])
  
  if len(A[A[:,0]=='True']) == 0:
    st.info('Hãy chọn 2 hoặc 3 đặc trưng mà bạn muốn.')
    
  elif len(A[A[:,0]=='True']) == 1:
    st.info('Bạn đã chọn: '+A[A[:,0]=='True',1][0]+'. Xin hãy chọn 1 hoặc 2 cái nữa.')
    
  elif len(A[A[:,0]=='True']) == 2:
    model = LogisticRegression()
    model.fit(X, y)
    weights = model.coef_[0]
    bias = model.intercept_[0]
    w1, w2 = weights
    
    x = np.array([0,10])
    fig = plt.figure(figsize=(8,8))
    for i in np.unique(y):
      plt.scatter(X[y==i,0],X[y==i,1])
    plt.xlabel(A[:,1][0])
    plt.ylabel(A[:,1][1])
    plt.plot(x,-(w1*x+bias)/w2)
    plt.legend(np.unique(y))
    st.pyplot(fig)
   
  else:
    st.error('Xin lỗi, bạn chỉ được chọn 2 hoặc 3 đặc trưng thôi. Xin hãy chọn lại.')
  
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
