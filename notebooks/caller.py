import sys
import streamlit as st
import pandas as pd
import numpy as np
from something import sayHey
sys.path.append('../')
from scripts.test import testfunc, removeText

st.write("hello")

name = st.text_input("Enter Your Name: ")

clicked = removeText(st)

if(clicked):
    testfunc('',st)
else:
    testfunc(name,st)

url = 'https://drive.google.com/uc?id=10rUiDQnhFUw_c43vHCpMFQweRtstpi2p'
data = pd.read_csv(url)
st.write(data)

# chart_data = pd.DataFrame(
#     np.random.randn()
# )

#sayHello(st)
sayHey(st)