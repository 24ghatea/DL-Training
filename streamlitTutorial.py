import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello,Streamlit !")
st.write(":streamlit: This is your first streamlit app")
st.text("Lets get strted")

#conditionnal logic with widgets
name = st.text_input("Enter your name")
if st.button("Greet"):
    st.success(f"Hello,{name}!")

#Displaying Data and charts
df=pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
st.line_chart(df)
st.bar_chart(df)

#File uploading and caching topics
upload_file = st.file_uploader("Choose a CSV file", type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.title("Text and Markdown Demo")
st.header("This-is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, `Code`, [Link](https://streamlit.io)")
st. code("for i in range(5): print(i)", language="python")

st.code("for i in range(5): print(i)", language="python")

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("show details"):
    st.info("Here are some details ...")

option=st.radio("choose view",["show chart","show table"])
if option=="show chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted =st.form_submit_button("Login")

    if submitted:
        st.success(f"Logged in as {username}!")

    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit Logo", width=200)
    st.video("https://www.youtube.com/watch?v=JwSS70SZdyM", format="video/mp4", start_time=0)
