import streamlit as st
import numpy as np
from df_change import df_change


ts = ['Taylor Swift', 'Kanye West', 'Justin Bieber', 'Selena Gomez', 'Kim Kardashian']
options = st.multiselect('Your favorite celebrity', ts)
st.write('Wow, you chose:',len(options))
st.write(options)
