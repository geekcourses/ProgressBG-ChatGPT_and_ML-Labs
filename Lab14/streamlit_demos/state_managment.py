import streamlit as st

# Demonstration of incorrect state management
# count = 0
# if st.button("Increment"):
#     count += 1

# st.write(f"Count: {count}") # Will ALWAYS be 1 after click, then back to 0!

# Correct way using st.session_state
if 'count' not in st.session_state:
    st.session_state['count'] = 0

if st.button("Increment"):
    st.session_state['count'] += 1

st.write(f"Count: {st.session_state['count']}")