import streamlit as st
from argon2 import PasswordHasher, exceptions

# Argon2 Password Hasher
ph = PasswordHasher()

# Streamlit UI
st.title("Password Hashing with Argon2")

# Input fields for username and password
username = st.text_input("Enter your username")
password = st.text_input("Enter your password", type="password")

# Button to trigger hashing
if st.button("Hash Password"):
    if not username or not password:
        st.error("Username and password are required.")
    else:
        try:
            # Hash the username and password
            uhash = ph.hash(username)
            phash = ph.hash(password)

            # Display the hashed values
            st.success("Successfully hashed the credentials.")
            st.write("Hashed Username:", uhash)
            st.write("Hashed Password:", phash)

        except Exception as e:
            st.error(f"Error during hashing: {e}")

# Additional info
st.write(
    "This app uses Argon2 to securely hash the username and password."
)
