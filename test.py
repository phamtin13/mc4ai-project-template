import streamlit as st
import numpy as np
from df_change import df_change

dfmid = df_change()
check = np.array([st.checkbox(i) for i in np.unique(dfmid['Subject'])])
A = np.stack((check,np.unique(dfmid['Subject']))).T
st.write(A)
needrop = []
for i in A:
  if i[0] is False:
    needrop += np.where(dfmid['Subject']==i[1])[0].tolist()
print(len(needrop))
dfmid.drop(needrop, inplace=True)
st.write(needrop)
