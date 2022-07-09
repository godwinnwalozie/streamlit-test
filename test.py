import streamlit as st
import pandas as pd

st.title("Hello")

file = pd.read_csv(r"/home/mazi/Data_Science_ML/streamlit-test/conf_max_df.csv")
st.write(file)
