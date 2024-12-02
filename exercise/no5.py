import streamlit as st

number = st.number_input("Pick a number", value=None, placeholder="Type a number")
st.write("The current number is ", number)

email = st.text_input("Email Address")

date = st.date_input("Travelling Date")

Time = st.time_input("Schoo Time")

txt = st.text_area("Descrption")
st.write(f"You wrote {len(txt)} characters.")

fu = st.file_uploader("Upload a Photo")

color = st.color_picker("Choose your favourite Color")