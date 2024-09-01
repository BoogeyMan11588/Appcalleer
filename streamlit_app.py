import streamlit as st

# App title
st.title("App Caller")

# Text input
name = st.text_input("Enter your name")

# Button
if st.button("Submit"):
    st.write(f"Hello, {name}!")

# Additional content
st.write(
    ""
)

st.write(
    ""
)
