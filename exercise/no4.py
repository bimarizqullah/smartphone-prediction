import streamlit as st

st.checkbox('yes')

st.button('Click')


gender = st.radio(
    'Pick your gender',
      ["Male", "Female"],
      captions=[
          "yeah, you're Male",
          "Of course you're Female"
      ],
)

if gender == (":Male"):
    st.write('You Selected:' , gender)
else:
    st.write('You Selected:', gender)


option = st.selectbox(
'Pick Your Gender',
("Male", "Female"),
)

st.write("You Selected:", option)

planet = st.selectbox(
    'Choose a Planet',
    ("Mercurius", "Venus", "Earth", "Mars",
    "Jupiter","Saturnus","Uranus","Neptunus"),
    index = None,
    placeholder = "Choose an Options..."
)

st.write("You Selected:", planet)


st.select_slider(
    'Pick a Mark',
    options=[
        "Bad",
        "Good",
        "Excellent"
    ]
)

st.select_slider(
    'Pick a Number',
    options=[
    1,2,3,4,5,
    6,7,8,9,10,
    11,12,13,14,15,
    16,17,18,19,20]
)
