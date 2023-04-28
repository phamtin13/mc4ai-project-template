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

ts = ['Taylor Swift', 'Kanye West', 'Justin Bieber', 'Selena Gomez']
options = st.multiselect('Your favorite celebrity', ts)
st.write('Wow, you chose:',len(options))

uniday = np.unique(dfmid['Part of day']).tolist()
options = st.multiselect('Buổi', uniday)
if len(options) == 1:
  for i in options:
    uniday.remove(i)
    A_day = np.stack(([False]*len(uniday),uniday,['Part of day']*len(uniday))).T
else:
  A_day = np.stack(([True]*len(uniday),uniday,['Part of day']*len(uniday))).T
