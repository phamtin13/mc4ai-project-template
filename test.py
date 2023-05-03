import streamlit as st
import numpy as np
from df_change import df_change
dfmid = df_change()
uniday = np.unique(dfmid['Part of day'])[::-1].tolist()
options = st.multiselect('Buổi:', uniday)
if len(options) != 0 and len(options) != len(uniday):
  #for i in options:
    #uniday.remove(i)
  #A_day = np.stack((['False']*len(uniday),uniday,['Part of day']*len(uniday))).T
  st.write('Khác')
else:
  #A_day = np.stack((['True']*len(uniday),uniday,['Part of day']*len(uniday))).T
  st.write('Giống')
st.write(len(uniday))
st.write(len(options))
st.write(options)
st.write(A_day)
