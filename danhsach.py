import pandas as pd
import streamlit as st
def danhsach():
  df = pd.read_csv("py4ai-score.csv", low_memory=False)
  dfmid = df.copy()
  COLS = dfmid.columns.values.tolist().copy()
  def gen(row):
    if row == 'M':
      return 'Nam'
    else:
      return 'Nữ'
  dfmid['Gen'] = dfmid.apply(gen, axis=1)
  st.write(dfmid.shape)
danhsach()
