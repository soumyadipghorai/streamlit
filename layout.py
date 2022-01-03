import streamlit as st 

st.title('Registration Form')

 
# function returns a container object 
first, last = st.columns(2) # we need 2 cols here
first.text_input('First Name')
last.text_input('Last Name')

email, mob = st.columns([3,1]) # list will devide the contaier in 3:1
email.text_input('Email ID')
mob.text_input('Phone number')

user_name, password, confirm_password = st.columns(3)
user_name = st.text_input('User name')
password = st.text_input('Password', type="password")
confirm_password = st.text_input('confirm password', type = "password")

check_box, blank, submit = st.columns(3)
check_box.checkbox('I agree')
submit.button('Submit')
