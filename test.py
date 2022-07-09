import streamlit as st
import pandas as pd

st.title("Hello")

file = pd.read_csv("/home/mazi/Data_Science_ML/ML--streamlit_stroke_prediction/pages/data/conf_max_df.csv")
st.write(file)