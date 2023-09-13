import streamlit as st
import functions

# Initialize session state variables
if "new_todo" not in st.session_state:
    st.session_state.new_todo = ""

todos = functions.get_todos()


def add_todo():
    todo = st.session_state.new_todo + "\n"
    todos.append(todo)
    functions.write_todos(todos)

    # Clear the input field after adding a new todo
    st.session_state.new_todo = ""


st.title("Todo App")
st.subheader("What are you waiting for?")
st.write("How about you get your work done?")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(
        todo, key=f"checkbox_{index}"
    )  # Use a unique key based on index
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"checkbox_{index}"]
        st.experimental_rerun()

# st.text_input(
#     label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo"
# )

st.text_input(
    label="New Todo:", placeholder="Add new todo...", on_change=add_todo, key="new_todo"
)
