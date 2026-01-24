import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Dashboard',
    page_icon="🚦",
)


st.write("# Dashboard The Fremont Bridge Bicycle Counter! 🚦")

st.sidebar.success("Select a option above.")

@st.cache_data
def load_dataset():

    df = pd.read_csv('df_fremont.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df

df = load_dataset()
st.dataframe(df)
