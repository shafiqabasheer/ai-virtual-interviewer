import streamlit as st

# Dummy user data
users = {
    "admin": "1234",
    "user": "abcd"
}

# Login function
def login():
    st.title("AI Virtual Interviewer - Login")
    email = st.text_input("email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email in users and users[email] == password:
            st.success(f"Welcome, {email}!")
            return True
        else:
            st.error("Invalid email or password")
            return False
    return False

# Main code
if login():
    st.write("### Interviewer Page Starts Here...")
    # You can continue your app here (e.g., questions, ML parts, etc.)
else:
    st.stop()  # Stops app until valid login
