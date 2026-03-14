import streamlit as st
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

st.Page("pages/create_account.py")

st.title("Register for an account:")

def run_register(username, password):
    cursor.execute(
        "INSERT INTO users (username, password, fname, surname, email)"
        "VALUES (?, ?, ?, ?, ?)",
        (username, password, fName, sName, uniEmail)
    )

with st.form("register_form"):
    st.write("Register Form:")
    fName = st.text_input("First Name: ", placeholder = "First Name Here...")
    sName = st.text_input("Second Name: ", placeholder = "Surname Name Here...")
    username = st.text_input("Username: ", placeholder = "Username Here...")
    uniEmail = st.text_input("Email (university):", placeholder = "Uni email Here...")

    
    password = st.text_input("Password:", type = "password", placeholder = "Password Here...")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Thank you for creating an account!")
