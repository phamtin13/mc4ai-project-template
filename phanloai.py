import streamlit as st
import numpy as np
from df_change import df_change
from sklearn.cluster import KMeans
import plotly.graph_objects as go

def phanloai():
  dfmid = df_change()
  dfmid.rename(columns={'S6' : 'Midterm Exam','S10' : 'Final Exam'}, inplace=True)
  check_sub = []
  cols = st.columns(5)
  for i in range(2):
    for j in range(6):
      check_sub.append(str(cols[j].checkbox(unisub[6*i+j],value=True,key=str(unisub[6*i+j])+' key')))
  A_sub = np.stack((check_sub,unisub,['Subject']*len(unisub))).T

  
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
