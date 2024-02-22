import streamlit as st
import pandas as pd


st.set_page_config(
    page_title='View Data',
    page_icon = ':)',
    layout='wide'
)
st.title('Data Page')
df = pd.read_csv('data_churn.csv')
st.dataframe(df)g