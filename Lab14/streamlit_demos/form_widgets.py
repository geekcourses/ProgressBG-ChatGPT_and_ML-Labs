import streamlit as st


with st.form("my_form"):
    st.write("Inside the form")

    user_name = st.text_input("user name")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val, "name", user_name)