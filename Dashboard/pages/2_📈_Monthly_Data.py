import streamlit as st
import pandas as pd



st.set_page_config(page_title='Monthly Data', page_icon="📈")

st.markdown("#### Monthly Data")
st.sidebar.success('Monthly Data')

@st.cache_data
def load_dataset():

    df = pd.read_csv('df_fremont.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    return df

df = load_dataset()
month = df['Total'].resample('M').sum()
dfmonth = pd.DataFrame({'total': month})

month_total = dfmonth.groupby(dfmonth.index.month)['total'].sum()
month_mean = dfmonth.groupby(dfmonth.index.month)['total'].mean()

left, right = st.columns(2, border=True)


left.markdown("Total by Month",text_alignment="center")
left.bar_chart(month_total, x_label='month', y_label='Total bicycle', color= "#ffaa0088", stack=False)

right.markdown("Total by Month",text_alignment="center")
right.line_chart(month_total)

left.markdown("Average by Month",text_alignment="center")
left.bar_chart(month_mean, x_label='month', y_label='Total bicycle', color= "#ffaa0088", stack=False)

right.markdown("Average by Month",text_alignment="center")
right.line_chart(month_mean)

df_total = pd.DataFrame({
    'Total by Month': month_total,
    'Average by Month': month_mean,
})

st.dataframe(df_total)