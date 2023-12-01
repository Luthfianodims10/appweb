import streamlit as st

st.write('st.button')

if st.button('say hello'):
    st.write('why hello there')
else:
    st.write('goodbye')