import streamlit as st
import numpy as np
from df_change import df_change

dfmid = df_change()
check = np.array([st.checkbox(i) for i in np.unique(dfmid['Subject'])])
A = np.stack((check,np.unique(dfmid['Subject']))).T
needrop = []
for i in A:
  if i[0] == False:
    needrop += np.where(dfmid['Subject']==i[1])[0].tolist()
dfmid.drop(needrop, inplace=True)
st.write(dfmid)
