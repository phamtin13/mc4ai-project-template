import streamlit as st
import numpy as np
import plotly.graph_objects as go
#import plotly.express as px
import plotly.graph_objects as go
from df_change import df_change
from sklearn.cluster import KMeans

def phannhom():
  dfmid = df_change()
  datas = np.linspace(0,10,100)
  dfmid.rename(columns={'S6' : 'Midterm Exam','S10' : 'Final Exam'}, inplace=True)
  slider = st.slider('Số nhóm:', min_value = 2, max_value = 5, step = 1)
  kmeans = KMeans(n_clusters=slider, n_init='auto')
  X = np.stack((dfmid['Homework'],dfmid['Midterm Exam'],dfmid['Final Exam'])).T
  kmeans.fit(X)
  labels = kmeans.labels_
  fig = go.Figure(data=[go.Surface(x=datas, y=datas, z=data)])
  #st.write(px.scatter_3d(dfmid, x = 'Homework', y = 'Midterm Exam', z = 'Final Exam', color = labels))
  for i in np.unique(labels):
    fig = go.Figure(data=[go.Surface(x=dfmid['Homework'][labels==i], y=dfmid['Midterm Exam'][labels==i], z=dfmid['Final Exam'][labels==i])])
  st.write(fig)
  
phannhom()
