from modules import functions
import matplotlib
matplotlib.use('Agg')
import streamlit as st

custom_css = """
<style>
    /* Target the container for the text input */
    div[data-testid="stTextInput"] {
        border: 2px solid orange;
        border-radius: 5px; /* Optional: adds rounded corners */
        padding: 5px; /* Optional: adds some space inside */
    }

    /* Target the scrollable container */
    div[data-testid="stContainer"] {
        border: 2px solid orange !important;
        border-radius: 5px;
    }
</style>
"""

todos = functions.read_todos()

def add_todo():
    todo_item = st.session_state["new_todo"]
    print(f"Adding todo: {todo_item}")
    todos.append(todo_item + '\n')
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def complete_todo(todo_item):
    print(f"Completing todo: {todo_item}")
    todos.remove(todo_item)
    functions.write_todos(todos)
    del st.session_state[todo_item]


st.title("ToDo App")

with st.container(height=500, ):
    for todo in todos:
        st.checkbox(todo, key=todo, on_change=complete_todo, args=(todo,))

st.text_input(label='', placeholder="Enter a todo item...", on_change=add_todo, key='new_todo')

