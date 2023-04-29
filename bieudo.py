import streamlit as st
import numpy as np
import plotly.express as px
from df_change import df_change

dfmid = df_change()

tab1, tab2 = st.tabs(["Số lượng học sinh", "Điểm"])

with tab1:
  def pie(df,a):
    return px.pie(df, names=a)
  
  nhanxet = ['Gen','* Tín\ 
                    *hưng']
  st.write(nhanxet[1])
