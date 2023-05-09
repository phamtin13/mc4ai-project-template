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
  st.subheader('Phân tích điểm số để biết đậu hoặc rớt:')
  check = []
  cols = st.columns(3)
  for i in range(3):
    check.append(str(cols[i].checkbox(options[i],key=str(options[i])+' key')))
  A = np.stack((check,options)).T
  X = np.array(dfmid[A[A[:,0]=='True',1]])
  y = np.array(dfmid['Fail or Pass'])
  choice = A[A[:,0]=='True',1]
  model = LogisticRegression()
  
  if len(A[A[:,0]=='True']) == 0:
    st.info('Hãy chọn 2 hoặc 3 đặc trưng để phân tích xem điểm số phải nằm trong khoảng nào mới có cơ hội đậu khoá học (GPA phải tối thiểu là 6 điểm).')
    
  elif len(A[A[:,0]=='True']) == 1:
    st.info('Bạn đã chọn: '+choice[0]+'. Xin hãy chọn 1 hoặc 2 cái nữa.')
    
  elif len(A[A[:,0]=='True']) == 2:
    model.fit(X, y)
    weights = model.coef_[0]
    bias = model.intercept_[0]
    w1, w2 = weights
    
    x = np.array([0,10])
    fig = plt.figure(figsize=(8,8))
    for i in np.unique(y):
      plt.scatter(X[y==i,0],X[y==i,1])
    plt.xlabel(choice[0])
    plt.ylabel(choice[1])
    plt.plot(x,-(w1*x+bias)/w2)
    plt.legend(np.unique(y))
    st.pyplot(fig)
    st.success('Score: '+str(np.round(model.score(X, y)*100,1))+'%')
   
  else:
    model.fit(X, y)
    weights = model.coef_[0]
    bias = model.intercept_[0]
    w1, w2, w3 = weights
    
    data = []
    for i in np.unique(y):
      data.append(go.Scatter3d(x=X[y==i,0], y=X[y==i,1], z=X[y==i,2], mode='markers',name = i))
    
    x = np.linspace(0, 10, 100)
    y1 = np.linspace(0, 10, 100)

    xx, yy = np.meshgrid(x, y1)
    xy = np.c_[xx.ravel(), yy.ravel()]  
    z = -(w1*xy[:,0] + w2*xy[:,1]+bias)/w3
    z = z.reshape(xx.shape)
    data.append(go.Surface(x=x, y=y1, z=z))
    fig = go.Figure(data=data)
    fig.update_layout(showlegend=True,scene = dict(xaxis = dict(title=choice[0]),yaxis = dict(title=choice[1]),zaxis = dict(title=choice[2])))
    st.plotly_chart(fig)
    st.success('Score: '+str(np.round(model.score(X, y)*100,1))+'%')
    st.balloons()
  
phanloai()
