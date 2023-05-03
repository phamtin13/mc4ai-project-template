import streamlit as st
import numpy as np
from df_change import df_change
dfmid = df_change()
uniday = np.unique(dfmid['Part of day'])[::-1].tolist()
options = st.multiselect('Buổi:', uniday)
if len(options) == 0 or len(options) == len(uniday):
  A_day = np.stack((['True']*len(uniday),uniday,['Part of day']*len(uniday))).T
else:
  difday = list(set(uniday) - set(options))
  A_day = np.stack((['False']*len(difday),difday,['Part of day']*len(difday))).T
st.write(uniday)
st.write(len(uniday))
st.write(options)
st.write(len(options))
st.write(A_day)
