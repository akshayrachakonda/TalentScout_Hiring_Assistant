import streamlit as st

def initialize_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "step" not in st.session_state:
        st.session_state.step = "greet"

    if "candidate" not in st.session_state:
        st.session_state.candidate = {
            "name": "",
            "email": "",
            "phone": "",
            "experience": "",
            "role": "",
            "location": "",
            "tech_stack": ""
        }