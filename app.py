import streamlit as st

# Dummy user data
users = {
    "admin": "1234",
    "user": "abcd"
}

# Login function
def login():
    st.title("AI Virtual Interviewer - Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.success(f"Welcome, {username}!")
            return True
        else:
            st.error("Invalid username or password")
            return False
    return False

# Main code
if login():
    st.write("### Interviewer Page Starts Here...")
    # You can continue your app here (e.g., questions, ML parts, etc.)
else:
    st.stop()  # Stops app until valid login
