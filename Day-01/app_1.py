import streamlit as st
import time


# Title:
st.title("This is a Title")

# Header:
st.header("This is a header")

# Sub Header:
st.subheader("This is a sub-header")

# Information Details:
st.info("This is info")

# Warning Details:
st.warning("This is warning")

# Write:
st.write("This is write: This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, write() has some unique propertie")
st.write("Coding Format: ", range(0, 100)) # in coding format.

# Error Message:
st.error("This is error message")

# Success Message:
st.success("This is success messages")

# Markdown:
st.markdown("# Markdown-1")
st.markdown("## Markdown-2")
st.markdown("### Markdown-2")
st.markdown(":moon:")

# Text:
st.text("I am learning streamlit text function")

# Caption:
st.caption("This is caption")

# Display Mathematical function:
st.latex(r'''y = a + bx^2 + c''')



### Widget:

# Checkbox:
ch = st.checkbox("check out!")
# print(ch)

# Button:
st.button("Submit")

# Radio Button:
gn = st.radio("Select your gender", ['male', 'female', 'others'])
# print(gn)

# Select Box (Single Selection):
sc = st.selectbox("Pick upu your course", ['ML', 'DL', 'NLP', 'CV'])
# print(sc)

# Multi-Select Box (Multiple Selection):
msc = st.multiselect("Choose Departments", ['eng', 'beng', 'his', 'geo'])
# print(msc)

# Select Slider: 
scl = st.select_slider("Rating", [0,1,2,3,4])
# print(scl)

# Slider:
st.slider("Select the Number from Slider", 0, 100)


### Inputs:

# Number Input:
st.number_input("Enter any number")

# Text Input:
st.text_input("Enter any text")

# Date Input:
st.date_input("ENter your DOB")

# Time Input:
st.time_input("Enter Time Input")

# Text Area:
st.text_area("Enter Description: ")

# FIle Upload:
st.file_uploader("Upload any file")

# Color picker:
st.color_picker("Pick up any Color")

# Progress:
st.progress(90, text="Progress")

# splinner (It isused to display temporary wating during execution)
with st.spinner('Wait for it...'):
    time.sleep(1)
st.success('Done!')

# Ballons (for celebration)
st.balloons()

# Sidebar (left)
st.sidebar.title("Welcome")
st.sidebar.text_input("Enter your EMail")
st.sidebar.text_input("Password")
st.sidebar.button("Login")


### Data Visualization:
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(100, 2)/[50, 50] + [37.76, -122.4], columns=['lat', 'lon'])

# Bar Chart:
st.title("Bar Chart")
st.bar_chart(df)

# Line Chart:
st.title("Line Chart")
st.line_chart(df)

# Area Chart:
st.title("Area Chart")
st.area_chart(df)