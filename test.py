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
#st.write(dfmid)

ts = ['Taylor Swift', 'Kanye West', 'Justin Bieber', 'Selena Gomez']
options = st.multiselect('Your favorite celebrity', ts)
st.write('Wow, you chose:',len(options))

uniday = ['Sáng', 'Chiều', 'Trưa']
options = st.multiselect('Buổi', uniday)
if len(options) != 0 and len(options) != len(uniday):
  for i in options:
    uniday.remove(options)
  A_day = np.stack(([False]*len(uniday),uniday,['Part of day']*len(uniday))).T
else:
  A_day = np.stack(([True]*len(uniday),uniday,['Part of day']*len(uniday))).T
st.write(A_day)

dfmid = df_change()
#check_subject = np.array([st.checkbox(i) for i in np.unique(dfmid['Subject'])])
#A = np.stack((check,np.unique(dfmid['Subject']))).T
unisub = np.unique(dfmid['Subject']).tolist()
#for i in range(2):
  #for j in range(5):
    #for i in unisub:
      #st.checkbox(i)
      #unisub = unisub[1:]
      #break

unisub.remove('Khác')
unisub.append('Khác')
cols = st.columns(5)
for i in range(2):
  for j in range(5):
    cols[j].checkbox(unisub[5*i+j],key=unisub[5*i+j]+'key')
