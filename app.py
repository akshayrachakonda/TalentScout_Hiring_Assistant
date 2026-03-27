import streamlit as st
from state import initialize_state
from validators import validate_email, validate_phone
from prompts import generate_questions
import re
from prompts import fallback_response
from validators import validate_tech_stack
initialize_state()

st.title("TalentScout Hiring Assistant")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your response...")

if user_input:

    if user_input.lower() in ["exit", "quit", "bye"]:
        st.chat_message("assistant").write(
            "Thank you! Our team will contact you soon."
        )
        st.stop()
        
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    step = st.session_state.step
    candidate = st.session_state.candidate

    response = ""

    if step == "greet":
        response = "Hello! I am TalentScout AI. Let's start with your full name."
        st.session_state.step = "name"

    elif step == "name":
        candidate["name"] = user_input
        response = "Great! Please provide your email."
        st.session_state.step = "email"

    elif step == "email":
        if validate_email(user_input):
            candidate["email"] = user_input
            response = "Enter your phone number."
            st.session_state.step = "phone"
        else:
            response = "Invalid email. Please enter a valid email like example@gmail.com"

    elif step == "phone":
        if validate_phone(user_input):
            candidate["phone"] = user_input
            response = "Years of experience?"
            st.session_state.step = "experience"
        else:
            response = "Invalid phone number. Please enter a valid phone number."

    elif step == "experience":
        candidate["experience"] = user_input
        response = "Desired role?"
        st.session_state.step = "role"

    elif step == "role":
        candidate["role"] = user_input
        response = "Current location?"
        st.session_state.step = "location"

    elif step == "location":
        candidate["location"] = user_input
        response = "List your tech stack."
        st.session_state.step = "tech"

    elif step == "tech":

        tech_list = re.split(r"[, ]+", user_input)
        tech_list = [tech.strip() for tech in tech_list if tech]

        if not validate_tech_stack(tech_list):
            response = """
            Invalid tech stack.

            Please enter valid technologies like:
            Python, React, Node.js, MongoDB
            """
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            with st.chat_message("assistant"):
                st.write(response)

            st.stop()

        candidate["tech_stack"] = ", ".join(tech_list)

        with st.spinner("Generating technical questions..."):
            questions = generate_questions(
                candidate["tech_stack"],
                candidate["experience"]
            )
        
        if "❌" in questions or "⚠️" in questions:
            response = """
            ⚠️ Unable to generate questions right now.

            Please try again later.
            """
        else:
            response = f"""
            {questions}

            ✅ Thank you {candidate['name']}!

            📋 Summary:
            - Role: {candidate['role']}
            - Experience: {candidate['experience']} years
            - Tech Stack: {candidate['tech_stack']}

            🚀 Our team will review your profile and contact you soon.
            """

        st.session_state.step = "done"

    else:
        response = fallback_response()

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)