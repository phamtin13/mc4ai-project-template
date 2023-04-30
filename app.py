import streamlit as st
from danhsach import danhsach
from bieudo import bieudo
from phannhom import phannhom

def main():
  st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')
  tab1, tab2, tab3, tab4 = st.tabs(['Danh sách','Biểu đồ','Phân nhóm','Phân loại','Hi'])
  
  with tab1:
    danhsach()
  
  with tab2:
    bieudo()
 
  with tab3:
    phannhom()
    
main()
