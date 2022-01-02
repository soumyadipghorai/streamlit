from altair.vegalite.v4.schema.channels import Tooltip
import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import altair as alt 

data = pd.DataFrame(
    np.random.randn(100, 3), 
    columns = ['a', 'b', 'c']
)

chart = alt.Chart(data).mark_circle().encode(
    x = 'a', y = 'b', tooltip = ['a', 'b'] # tooltip makes it interactive 
)

st.map() # takes the center of the map and display 
# data frame must have lat and long col for map  

map_data = pd.DataFrame({
    'city' : ['a', 'b', 'c', 'd'],
    'lat' : [21.12232, 23.4354, 45.345243, 64.4434], 
    'lon' : [45.2343, 54.23341,35.23452,64.23432]
})

st.map(map_data) # red dots will be made according to the lat and long

# flow chart 
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

st.altair_chart(chart, use_container_width= True) # uses the whole container width and make the plot bit larger 

st.line_chart(data) #plots an interactive line chart 

st.area_chart(data) # interactive area chart 

st.bar_chart(data) # interactive bar chart 

plt.scatter(data['a'], data['b']) # a for x-axis --> b for y-axis 
plt.title('scatter plot')
st.pyplot() # in regular python we use plt.show()

st.image('image.jpeg') # you can specify height = ... & width = ...

st.audio('demo.wav')

st.video('demo.mp4')

st.video('link') # this will embed the youtube video