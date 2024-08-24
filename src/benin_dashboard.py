import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from showDataHead import readData, stats
from dataCleanUp import removeComments

def show_analysis_benin():
    df = readData('benin')

    st.title('Solar Radiation Benin Dashboard')

    st.write(df)

    st.write('Statistics for benin')
    st.write(stats('benin'))

    st.write('Remove Comments')

    st.write(removeComments('benin'))

# Plot GHI over time
    st.subheader('GHI over Time')
    fig, ax = plt.subplots(figsize=(12, 6))
    df.plot(x='Timestamp', y='GHI', ax=ax)
    st.pyplot(fig)

# Plot histogram of GHI
    st.subheader('Histogram of GHI')
    fig, ax = plt.subplots(figsize=(10, 6))
    df['GHI'].hist(ax=ax, bins=20)
    st.pyplot(fig)
