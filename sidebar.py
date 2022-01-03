from logging import disable, warning
import streamlit as st 
import pandas as pd 
from matplotlib import pyplot as plt 
import time

# except write everything can be added in the sidebar 
plt.style.use('ggplot')

data = {
    'num' : [x for x in range(1,11)],
    'square' : [x**2 for x in range(1,11)], 
    'cube' : [x**3 for x in range(1,11)], 
    'twice' : [x*2 for x in range(1,11)],
    'thrice' : [x*3 for x in range(1,11)]
}

rad = st.sidebar.radio('Navigation', ['home', 'about us'])

if rad == 'home' : 
    df = pd.DataFrame(data = data)

    col = st.sidebar.multiselect('select a column', df.columns) # selectbox in the sidebar 

    try :
        plt.plot(df['num'], df[col])

        # !to disable warning
        st.set_option('deprecation.showPyplotGlobalUse', False)

        st.pyplot()

    except : 
        st.write('select from sidebar')

if rad == 'about us' :
    st.write('you are in the about us page')

    # progress bar
    progress = st.progress(0)
    for i in range(100) : 
        time.sleep(0.1)
        progress.progress(i+1)

    st.balloons()

    st.error('Error')
    st.success('show Success')
    st.info('show info')
    st.exception(RuntimeError('This is an error'))
    st.warning('this is a warning')