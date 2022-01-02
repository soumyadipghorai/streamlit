import streamlit as st 
import pandas as pd 
import numpy as np 
import time 

a = [1,2,3,4,5,6,7,8]

n = np.array(a)

nd = n.reshape((2,4))

value_dict = {
    "name" : ["ghorai"],  # values of dict must be list here 
    "age" : [22], 
    "city" : ["kolkata"]
}

data = pd.read_csv('dataset/netflix_titles.csv')
# print(data) ## prints in the console 

st.dataframe(a)
 
st.dataframe(n)

st.dataframe(nd)

st.dataframe(value_dict)

st.dataframe(data.head(), width= 500, height = 200)

st.table(data.head()) # here it shows all the data --> represents better small data

st.json(value_dict)

st.write(data) # this will by default format the data in specific type

@st.cache 
def ret_time() : 
    time.sleep(5)
    return time
# this will save this function in cache memory 
# next when this function will be called with the same parameter it will give the output in no time 
# this will make the app way faster 


if st.checkbox("1") : 
    st.write(ret_time())

if st.checkbox("2") : 
    st.write(ret_time())