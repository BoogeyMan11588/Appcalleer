import streamlit as st
from argon2 import PasswordHasher, exceptions

# Argon2 Password Hasher
ph = PasswordHasher()

# Streamlit UI
st.title("Password Hashing with Argon2- enter a username and password to get started!")

# Input fields for username and password
username = st.text_input("Enter a username")
password = st.text_input("Enter a password", type="password")

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
            st.success("We successfully hashed the credentials.")
            st.write("Your hashed Username:", uhash)
            st.write("Your hashed Password:", phash)

        except Exception as e:
            st.error(f"Error during hashing: {e}")

# Additional info
st.write(
    "This app uses Argon2 to securely hash your username and password."
)
