import streamlit as st
import numpy as np
import plotly.express as px
from df_change import df_change
from sklearn.cluster import KMeans

def phannhom():
  dfmid = df_change()
  x = np.linspace(0, 10, 100)
  y = np.linspace(0, 10, 100)
  z = np.linspace(0, 10, 100)
  slider = st.slider('Số nhóm:', min_value = 2, max_value = 5, step = 1)
  kmeans = KMeans(n_clusters=slider, n_init='auto')
  X = np.stack((dfmid['Homework'],dfmid['S6'],dfmid['S10'])).T
  kmeans.fit(X)
  st.write(px.scatter_3d(dfmid, x = 'Homework', y = 'S6', z = 'S10', color = kmeans.labels_))

phannhom()
