import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Dashboard',
    page_icon="🚦",
)


st.write("#### Dashboard The Fremont Bridge Bicycle Counter! 🚦")

st.sidebar.success("Select a option above.")

@st.cache_data
def load_dataset():

    df = pd.read_csv('Fremont_Bridge_Bicycle_Counter.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.rename({'Fremont Bridge Sidewalks, south of N 34th St Total' : 'Total'}, axis=1, inplace=True)
    df.rename({'Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk' : 'West Sidewalk'}, axis=1, inplace=True)
    df.rename({'Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk' : 'East Sidewalk'}, axis=1, inplace=True)
    return df

df = load_dataset()
st.dataframe(df)

