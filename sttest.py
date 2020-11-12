import streamlit as st
x = st.slider('x')
st.write('The Price of this chair is: $', x)
y = st.selectbox('Select one',('Cat', 'Dog', 'Zebra'))
st.write("The world's best ", y)
if st.button('Touch Me Not!'):
    st.write('You shall not pass!')