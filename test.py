import streamlit as st
import numpy as np
from df_change import df_change

A = [st.checkbox(i) for i in np.unique(dfmid['Subject'])]
