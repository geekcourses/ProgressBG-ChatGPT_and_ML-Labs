import streamlit as st
import time
import random

st.title("Fake LLM Chat")

# 1. Initialize history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. Render history (Redraw previous messages)
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 3. Handle new input
if prompt := st.chat_input("Say something..."):
    # A. Display User Message
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # B. Generate & Display Assistant Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1)  # Fake delay

            # Simple fake logic to mimic intelligence
            response_text = f"You said: {prompt}."

            st.write(response_text)

    # C. Save Assistant Response to history
    st.session_state.messages.append({"role": "assistant", "content": response_text})