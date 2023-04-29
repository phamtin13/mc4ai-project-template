import streamlit as st
import numpy as np
from df_change import df_change
from sklearn.cluster import KMeans

def phannhom():
  dfmid = df_change()
  slider = st.slider('Số nhóm:', min_value = 2, max_value = 5, step = 1)
  kmeans = KMeans(n_clusters=slider, n_init='auto')
  st.write(dfmid)

phannhom()
