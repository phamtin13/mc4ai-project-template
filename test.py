import streamlit as st
import numpy as np
from df_change import df_change
dfmid = df_change()
uniday = np.unique(dfmid['Part of day'])[::-1].tolist()
options = st.multiselect('Buổi:', uniday)
if len(options) == 0 or len(options) == len(uniday):
  st.write('Giống')
  #A_day = np.stack((['True']*len(uniday),uniday,['Part of day']*len(uniday))).T
else:
  st.write('Khác')
  #uniday.remove(options[0])
  #A_day = np.stack((['False']*len(uniday),uniday,['Part of day']*len(uniday))).T
st.write(uniday)
st.write(len(uniday))
st.write(options)
st.write(len(options))
#st.write(A_day)
