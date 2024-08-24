import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from benin_dashboard import show_analysis_benin
from togo_dashboard import show_analysis_togo
from sierraleone import show_analysis_sierra

page = st.sidebar.selectbox('Explore or Predict',["Benin", "Togo","Sierraleone"])
if page == "Benin":
    show_analysis_benin()
elif page == "Togo":
    show_analysis_togo()
elif page == "Sierraleone":
    show_analysis_sierra()