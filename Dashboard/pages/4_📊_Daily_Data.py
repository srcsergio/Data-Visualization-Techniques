import streamlit as st
import pandas as pd


st.set_page_config(page_title='Daily Data')

st.markdown("### Daily Data")
st.sidebar.success('Daily Data')

def load_dataset():
    df = pd.read_csv('df_fremont.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['time'] = df.index.time

    return df

df = load_dataset()

by_tyme_day = df.groupby('hour')['Total'].mean()
by_tyme = df.groupby(df.index.time)['Total'].mean()


left, right = st.columns(2, border=True)

left.markdown("Average hourly bicycle", text_alignment='center')
left.bar_chart(by_tyme_day, x_label='hour', y_label='Average hourly')

right.markdown("Average hourly bicycle",text_alignment="center")
right.line_chart(by_tyme_day, x_label='hour', y_label='Average hourly')

df_by_time_day= pd.DataFrame({'Average by hour': by_tyme})
st.write(df_by_time_day)