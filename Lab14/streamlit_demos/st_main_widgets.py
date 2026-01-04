import streamlit as st
import pandas as pd


st.header("Chart Examples")
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

with st.container(border=True):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.line_chart(df, use_container_width=True)

st.bar_chart(df)

st.header("Data Display Examples")
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

st.dataframe(df) # Interactive
st.table(df) # Static

with st.expander("More details"):
    st.write("Hidden details 1")
    st.write("Hidden details 2")


with st.container(border=True):
    st.write("This is inside a custom container.")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Chat Message Examples")
        st.chat_input("Enter your message")
        st.chat_message("user").write("Hello")
        st.chat_message("assistant").write("Hello")

    with col2:
        st.header("Input Widgets Examples")
        name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", min_value=0)
        choice = st.selectbox("Choose one", ["A", "B", "C"])
        slider = st.slider("Pick a value", 0, 100)
        checked = st.checkbox("I agree")
        button = st.button("Submit")

st.title("My Streamlit App")
st.header("Section Header")
st.subheader("Subsection")
st.text("Plain text")
st.markdown("**Markdown** is _supported_")

st.header("Media Examples")
st.image("./picture.webp")
st.audio("https://via.placeholder.com/150")
st.video("https://via.placeholder.com/150")