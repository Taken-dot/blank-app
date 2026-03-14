import streamlit as st
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

if 'user_id' not in st.session_state:
      st.warning("You cannot view your details, please log in!")
      st.stop()

user_id = st.session_state['user_id']

cursor.execute("SELECT username, password, fName, surname, email FROM users WHERE id = ?", (user_id))
user = cursor.fetchone()

if not user:
      st.error("Your record cannot be found!")
      st.stop()


user = username_in, password_in, first_name_in, second_name_in, email_in

with st.form("profile_form"):
        st.write("My Profile:")
        username = st.text_input("Username", value = username_in)
        password = st.text_input("Password:", type = "password", value = password_in)
        first_name = st.text_input("First Name:", value = first_name_in)
        second_name = st.text_input("Second Name:",value = second_name_in)
        email = st.text_input("Email:", value = email_in)

        submitted = st.form_submit_button("Submit")

        if submitted:
               cursor.execute("UPDATE users SET username = ?, password = ?, first_name = ?, second_name = ?, email = ? WHERE id = ?", (username, password, first_name, second_name, email, user_id))
               conn.commit()
               st.success("Your profile has bene updated!")
            
