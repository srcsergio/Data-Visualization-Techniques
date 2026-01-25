import streamlit as st
import pandas as pd
import altair as alt


st.set_page_config(page_title='Weekly Data', page_icon='📉')

st.markdown("# Weekly Data")
st.sidebar.success('Weekly Data')

st.write(
        """
        Weekly
"""
)

@st.cache_data
def load_dataset():

    df = pd.read_csv('df_fremont.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    return df

df = load_dataset()
weekly_total = df['Total'].resample('W').sum()
dfweekly = pd.DataFrame({'total': weekly_total})

left, right = st.columns(2, border=True)


left.markdown("Total by weekly",text_alignment="center")
left.bar_chart(dfweekly, x_label='month', y_label='Total bicycle', color= "#ffaa0088", stack=False)

right.markdown("Total by weekly",text_alignment="center")
right.line_chart(dfweekly)


st.dataframe(dfweekly)