import streamlit as st
import numpy as np
from df_change import df_change

dfmid = df_change()
check = np.array([st.checkbox(i) for i in np.unique(dfmid['Subject'])])
A = np.stack((check,np.unique(dfmid['Subject']))).T
st.write(A)
for i in A:
  if i[0] is True:
    dfmid = dfmid.loc[dfmid['Subject']==i[-1]]
st.write(dfmid)
