import streamlit as st
import time
import random
from argon2 import PasswordHasher, exceptions

# Argon2 Password Hasher
ph = PasswordHasher()

# Title with UI flare
st.title("🎉 Generate Argon2 hash's 🎉")

# Input fields for username and password
username = st.text_input("Enter a username")
password = st.text_input("Enter a password", type="password")

# Neon loading bar simulation (fake wait)
def neon_loading_bar():
    st.info("🔋 Preparing to hash your credentials...")
    progress = st.progress(0)
    wait_time = random.uniform(3, 7)
    for percent_complete in range(100):
        time.sleep(wait_time / 100)
        progress.progress(percent_complete + 1)

# Button to trigger hashing
if st.button("Hash it 🚀"):
    if not username or not password:
        st.error("Username and password are required. 🙄")
        st.markdown("🙄 Please enter both username and password.")
    else:
        neon_loading_bar()  # Show the neon loading bar

        try:
            # Hash the username and password
            uhash = ph.hash(username)
            phash = ph.hash(password)

            # Display the hashed values
            st.success("We successfully hashed the credentials!")
            st.write("Hashed Username:", uhash)
            st.write("Hashed Password:", phash)

            # Fireworks animation after hashing
            st.balloons()  # This is the built-in Streamlit fireworks effect

        except Exception as e:
            st.error(f"Error during hashing: {e}")

# Additional info
st.write(
    "🔒 This app uses Argon2 to securely hash your username and password."
)
