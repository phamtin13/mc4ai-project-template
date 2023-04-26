import pandas as pd
import streamlit as st
df = pd.read_csv("py4ai-score.csv", low_memory=False)
st.text('This is a text')
st.code('x = 5\nprint(x)')
st.latex('x^2 + \sqrt{y} = \pi')
st.write(df) 
