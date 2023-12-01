import streamlit as st

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender' , ['Male' , 'Female'])
st.selectbox('Pick your gender' , ['Male' , 'Female'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excelent'])
st.slider('Pick a number', 0, 50)