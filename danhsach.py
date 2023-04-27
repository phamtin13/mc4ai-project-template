import pandas as pd
import streamlit as st
def danhsach():
  df = pd.read_csv("py4ai-score.csv", low_memory=False)
  dfmid = df.copy()
  COLS = dfmid.columns.values.tolist().copy()
  def gen(row):
    if row[1] == 'M':
      return 'Nam'
    else:
      return 'Nữ'
  dfmid['Gen'] = dfmid.apply(gen, axis=1)
  st.title("Todo list app")

# 1. Create a variable to store todos.
  if not 'todolist' in st.session_state:
    st.session_state.todolist = []

# 2. Prompt the user in the form
  with st.form(key='form'):
    todo = st.text_input(label='Enter todo description')
    is_submit = st.form_submit_button('submit')

# 3. Store todo in todolist when submit button is hit.
  if is_submit:
    st.session_state.todolist.append(todo)
    
# 4. Display the contents of todolist
  with st.expander(label='List of todos', expanded=True):
    for i, todo_text in enumerate(st.session_state.todolist):
      st.checkbox(label=f'{todo_text}', key=i)
danhsach()
