import streamlit as st

st.title('Widgets')

if st.button('PAY NOW') : # buttons will return bool value 
    st.write('thanks a lot') # if clicked display this

name = st.text_input("Type your name")
st.write(name)

address = st.text_area('Enter your address')
# print(address)
st.write(address)

st.date_input("enter a date")

st.time_input("enter a time")

if st.checkbox('you accept the given T&C', value = True) : # by default the box will be checked 
    st.write('thanks')

v1 = st.radio("colors", ['r', 'g', 'b'], index = 1)
# list of options are given 
# index selects the 1th index by default 

v2 = st.selectbox("colors", ['r', 'g', 'b'], index = 0)
# list of options are given 
# index selects the 0th index by default 

v3 = st.multiselect("colors", ['r', 'g', 'b'])

v4 = st.slider('age', min_value= 18, max_value= 60, value= 30, step=2)

v5 = st.number_input('number', min_value= 18.0, max_value= 60.0, value= 30.0, step=0.5) # here values should be float 

st.write(v1, v2, v3, v4, v5)

image = st.file_uploader('upload an image')
if image :
    st.image(image)