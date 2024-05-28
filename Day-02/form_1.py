import streamlit as st


# Form:
with st.form(key="form_1", clear_on_submit=False):
    st.title("My First Form")
    name = st.text_input(label="Enter Yor Name")
    email = st.text_input(label="Enter your Email")
    bio = st.text_area(label="Write Something about you")
    range = st.slider(label="Select Range", min_value=10, max_value=75)

    button = st.form_submit_button(label="Submit Form")
    if button:
        st.balloons()