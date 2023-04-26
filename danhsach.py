import pandas as pd
import streamlit as st
df = pd.read_csv("py4ai-score.csv", low_memory=False)
st.write(df) 
