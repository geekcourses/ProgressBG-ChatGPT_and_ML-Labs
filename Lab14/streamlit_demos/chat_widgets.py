import streamlit as st

# # inputs
# st.text_input("Enter your message")
# st.chat_input("Type your message here")

# # outputs
# st.text("Chat Message Examples")
# st.chat_message("user").write("Hello, how are you?")
# st.chat_message("assistant").write("I'm good, thank you!")

# The script stops here and waits for the user
if prompt := st.chat_input("Type your message here..."):
    st.chat_message("user").write(f"Received: {prompt}")

