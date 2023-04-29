import streamlit as st
import numpy as np
import plotly.express as px
from df_change import df_change

dfmid = df_change()

tab1, tab2 = st.tabs(["Số lượng học sinh", "Điểm"])

with tab1:
  nhanxet = np.array([['Giới tính','Gen','Nhìn chung học sinh Nam hứng thú với AI hơn học sinh Nữ.'],
             ['Môn học','Subject','Khối chuyên Toán quan tâm đến AI nhiều nhất và khối chuyên Trung - Nhật ít quan tâm nhất.'],
             ['Lớp Python','PYTHON-CLASS','Số học sinh ở 2 buổi và 2 phòng học gần bằng nhau, nên giờ học là hợp lý, đáp ứng được nhu cầu của tất cả học sinh.'],
             ['Khối lớp','Grade','Số lượng học sinh lớp 10 tham gia khoá PY4AI là nhiều nhất và số lượng học sinh lớp 12 là ít nhất.']])
  
  option = st.radio('Phân tích biểu đồ hình tròn theo:', nhanxet[:,0], horizontal=True)
  st.write(px.pie(dfmid, names = nhanxet[:,1][nhanxet[:,0]==option][0]))
  st.success('Kết luận: '+nhanxet[:,2][nhanxet[:,0]==option][0])
  
