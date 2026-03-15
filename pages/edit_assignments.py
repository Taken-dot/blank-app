import streamlit as st
import sqlite3
import pandas as pd
from header import show_header

# ---------------------------------------------------
# Page configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Track Together",
    page_icon="👾",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Track Together. Made by Aparna, Tabitha, Tristan."
    }
)

show_header()

user_id = st.session_state.get("user_id")

if (user_id == None):
    st.switch_page("streamlit_app.py")


# ---------------------------------------------------
# Database connection
# ---------------------------------------------------
conn = sqlite3.connect("assignments.db", check_same_thread=False)
cursor = conn.cursor()

assignment_id = st.session_state.get("edit_assignment")

# Fetch the assignment to edit
assignment_query = "SELECT * FROM assignments WHERE id = ?"
assignment_df = pd.read_sql_query(assignment_query, conn, params=(assignment_id,))

st.title("Edit Assignment")

# ---------------------------------------------------
# Edit form
# ---------------------------------------------------
if not assignment_df.empty:
    assignment = assignment_df.iloc[0]

    with st.form("edit_assignment_form"):
        name = st.text_input("Assignment Name", value=assignment["name"], max_chars=65)
        module_name = st.text_input("Module Name", value=assignment["module_name"], max_chars=30)
        module_code = st.text_input("Module Code", value=assignment["module_code"], max_chars=6)
        due_date = st.date_input("Due Date", value=pd.to_datetime(assignment["due_date"]))

        submitted = st.form_submit_button("Save Changes")

        if submitted:
            cursor.execute(
                """
                UPDATE assignments
                SET name=?, module_name=?, module_code=?, due_date=?
                WHERE id=?
                """,
                (name, module_name, module_code, str(due_date), assignment_id)
            )
            conn.commit()

            st.success("Assignment successfully updated!")
            st.switch_page("pages/view_assignments.py")