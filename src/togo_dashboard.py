import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_analysis_togo():
    st.write('Togo')
    url = '../data/togo-dapaong_qc.csv'
    df = pd.read_csv(url)

    st.title('Solar Radiation Togo Dashboard')

    st.write(df.head())

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
