import streamlit as st
import numpy as np
import plotly.express as px
from df_change import df_change

dfmid = df_change()
COLS = dfmid.columns.values.tolist().copy()
COLS.remove('BONUS')

tab1, tab2 = st.tabs(["Số lượng học sinh", "Điểm"])

with tab1:
  nhanxet1 = np.array([['Giới tính','Gen','Nhìn chung học sinh Nam hứng thú với AI hơn học sinh Nữ.'],
             ['Môn học','Subject','Khối chuyên Toán quan tâm đến AI nhiều nhất và khối chuyên Trung - Nhật ít quan tâm nhất.'],
             ['Lớp Python','PYTHON-CLASS','Số học sinh ở 2 buổi và 2 phòng học gần bằng nhau, nên giờ học là hợp lý, đáp ứng được nhu cầu của tất cả học sinh.'],
             ['Khối lớp','Grade','Số lượng học sinh lớp 10 tham gia khoá PY4AI là nhiều nhất và số lượng học sinh lớp 12 là ít nhất.']])
  
  pies = st.radio('Phân tích biểu đồ số lượng học sinh theo:', nhanxet1[:,0], horizontal=True)
  st.write(px.pie(dfmid, names = nhanxet1[:,1][nhanxet1[:,0]==pies][0]))
  st.success('Kết luận: '+nhanxet1[:,2][nhanxet1[:,0]==pies][0])
  
with tab2:
  tys = np.array([['Biểu đồ cột (histogram)',px.histogram,'PYTHON-CLASS','Gen'],
                  ['Biểu đồ cột (histogram)',px.histogram,'Subject'],
                  ['Biểu đồ hộp (box)',px.box,'PYTHON-CLASS','Gen'],
                  ['Biểu đồ hộp (box)',px.box,'Subject']])
  sessions = np.array(COLS[4:15])
  types = st.radio('Phân tích điểm theo dạng:', np.unique(tys[:,0]), horizontal=True)
  option = st.radio('Điểm từng session:', sessions, horizontal=True)
  for i in tys:
    if i[0] == types:
      if len(i) == 4:
        st.write(i[1](dfmid, x = i[2], y = option, color = i[3]).update_layout(yaxis_title=option))
      else:
        st.write(i[1](dfmid, x = i[2], y = option).update_layout(yaxis_title=option))
                 
