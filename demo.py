import streamlit as st 

st.title('hello streamlit') 

st.header('header')

st.subheader('subheader')

st.text('learning this from scratch')

st.markdown(""" 
                # h1 tag
                ## h2 tag 
                ### h3 tag 
                #### h4 tag 
                ##### h5 tag 
                ###### h6 tag
                :moon: <br>
                :sunglasses: <br>
                ** bold **
                _italics_
 """, True) 
 # by default markdown doesn't read it as html
 # true makes the <br> tag as HTML 

# as latex uses lot of \\\ so we use row python string 
st.latex(r'''
a + ar + a r62 + a r63 + \cdots + a r^{n-1} = 
\sum_{k=0}^{n-1} ar^k = 
a \left(\frac{1-r^{n}}{1-r}\right)
''')

st.write("ghorai", "playlist") # will print all the values 

st.write("#ghorai") # used marked down 

st.write(st) #passing the module will give the documentations  

st.write(sum) # it will show how to use the function 

value_dict = {
    "name" : "ghorai", 
    "age" : 22, 
    "number" : 9832329029
}

st.write(value_dict) 