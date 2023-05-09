import streamlit as st
import numpy as np
import statistics
import plotly.express as px
from df_change import df_change
from nhanxet import nhanxet

def bieudo():
  dfmid = df_change()
  COLS = dfmid.columns.values.tolist().copy()
  COLS.remove('BONUS')

  tab1, tab2 = st.tabs(["Số lượng học sinh", "Điểm số"])

  with tab1:
    nhanxet1 = np.array([['Giới tính','Gen','Nhìn chung học sinh Nam có hứng thú với AI hơn học sinh Nữ.'],
               ['Môn học chính khoá','Subject','Khối chuyên Toán quan tâm đến AI nhất và khối chuyên Trung - Nhật ít quan tâm nhất.'],
               ['Lớp Python','PYTHON-CLASS','Số học sinh ở 2 buổi và 2 phòng học gần bằng nhau, nên giờ học là hợp lý, đáp ứng được nhu cầu của tất cả học sinh.'],
               ['Khối lớp','Grade','Số lượng học sinh lớp 10 tham gia khoá PY4AI là nhiều nhất và số lượng học sinh lớp 12 là ít nhất.']])

    pies = st.radio('Phân tích số lượng học sinh theo:', nhanxet1[:,0], horizontal=True)
    st.write(px.pie(dfmid, names = nhanxet1[:,1][nhanxet1[:,0]==pies][0]))
    st.info('Kết luận: '+nhanxet1[:,2][nhanxet1[:,0]==pies][0])

  with tab2:
    tys = np.array([['Biểu đồ cột (histogram)',px.histogram,'PYTHON-CLASS','Gen','lớp Python và giới tính','Tổng điểm ',sum,' có tổng điểm cao nhất là ',' có tổng điểm thấp nhất là '],
                    ['Biểu đồ cột (histogram)',px.histogram,'Subject',None,'môn học chính khoá','Tổng điểm ',sum,' có tổng điểm cao nhất là ',' có tổng điểm thấp nhất là '],
                    ['Biểu đồ hộp (box)',px.box,'PYTHON-CLASS','Gen','lớp Python và giới tính','Điểm ',statistics.median,' làm tốt nhất và trung bình đạt được tới ',' làm bài chưa được tốt nhất và trung bình chỉ đạt được '],
                    ['Biểu đồ hộp (box)',px.box,'Subject',None,'môn học chính khoá','Điểm ',statistics.median,' làm tốt nhất và trung bình đạt được tới ',' làm bài chưa được tốt nhất và trung bình chỉ đạt được ']])
    sessions = np.array(COLS[4:15])
    types = st.radio('Phân tích điểm theo dạng:', np.unique(tys[:,0]), horizontal=True)
    option = st.radio('Điểm từng session:', sessions, horizontal=True)
    
    for i in range(len(tys)):
      if tys[i][0] == types:
        st.subheader('Phân tích theo '+tys[i][4]+':')
        st.write(tys[i][1](dfmid, x = tys[i][2], y = option, color = tys[i][3]).update_layout(yaxis_title=tys[i][5]+option,showlegend=True))
        nhanxet2 = nhanxet(option,tys[i][6],tys[i][2],tys[i][7],tys[i][8])
        st.info('Kết luận:  \n'+nhanxet2)
        
bieudo()
