import streamlit as st
import numpy as np
from df_change import df_change
from sklearn.cluster import KMeans

def phanloai():
  dfmid = df_change()
  option = st.selectbox('Số đặc trưng', ('2 đặc trưng', '3 đặc trưng'))
  if option == '2 đặc trưng':
    pass
  
phanloai()
