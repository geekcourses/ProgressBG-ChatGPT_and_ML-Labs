import streamlit as st

st.sidebar.title("Side Navigation")
page = st.sidebar.selectbox("Select a page", ["Home", "Page 1", "Page 2"])

if page == "Home":
    st.title("Home")
elif page == "Page 1":
    st.title("Page 1")
elif page == "Page 2":
    st.title("Page 2")