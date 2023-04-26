import pandas as pd
import streamlit as st
def danhsach():
  df = pd.read_csv("py4ai-score.csv", low_memory=False)
  COLS = df.columns.values.tolist().copy()
  st.write(COLS)
danhsach()
