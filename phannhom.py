import streamlit as st
import numpy as np
import plotly.express as px
from df_change import df_change
from sklearn.cluster import KMeans

def phannhom():
  dfmid = df_change()
  dfmid.rename(columns={'S6' : 'Midterm Exam','S10' : 'Final Exam'}, inplace=True)
  slider = st.slider('Số nhóm:', min_value = 2, max_value = 5, step = 1)
  kmeans = KMeans(n_clusters=slider, n_init='auto')
  #X = np.stack((dfmid['Homework'],dfmid['Midterm Exam'],dfmid['Final Exam'])).T
  X = np.stack((dfmid['Homework'],dfmid['Midterm Exam'],dfmid['GPA'])).T
  kmeans.fit(X)
  #st.write(px.scatter_3d(dfmid, x = 'Homework', y = 'Midterm Exam', z = 'Final Exam', color = kmeans.labels_))
  st.write(px.scatter_3d(dfmid, x = 'Homework', y = 'Midterm Exam', z = 'GPA', color = kmeans.labels_))
  
  labels = np.array(['Nhóm '+str(i+1) for i in np.unique(kmeans.labels_)])
  kmeans.labels_ = np.array([str(i) for i in kmeans.labels_])
  
  for j in labels:
    df_need = dfmid.loc[kmeans.labels_==str(int(j[-1])-1)]
    df_new = df_need[['NAME', 'CLASS', 'Homework', 'Midterm Exam', 'Final Exam', 'GPA']]
  
    new = df_new['GPA']
    st.subheader(j+':')
    st.write('GPA cao nhất',new.max(),', thấp nhất',new.min(),', trung bình',np.round(new.mean(),1))
    st.write(df_new)
  
phannhom()
