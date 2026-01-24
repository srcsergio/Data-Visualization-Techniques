import streamlit as st
import time
import numpy as np
import pandas as pd

st.set_page_config(page_title="Summary Data", page_icon="📋")

st.markdown('##### Average and total annual number of bicycles traveling on the bridge.')
st.sidebar.success("Year Data")

st.write(
        """
        Summary
"""
    )

def get_weekend(day):
    weekend=0
    if day >= 5:
        weekend=1
    else:
        weekend = 0
    return weekend
        

def season(month):
    
    match month:
        case 12 | 1 | 2:
            return 'winter'  # Match winter month
        case 3 | 4 | 5:
            return 'spring' # Match spring months
        case 6 | 7 | 8:
            return 'summer' # Match summer months
        case _:
            return 'fall' 

@st.cache_data
def load_dataset():

    df = pd.read_csv('df_fremont.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    #resampling the data to daily
    df_daily = df[['Total']].resample('D').sum()
    df_daily['day_of_week'] = df_daily.index.dayofweek
    df_daily['month'] = df_daily.index.month
    df_daily['year'] = df_daily.index.year
    df_daily['weekend'] = df_daily['day_of_week'].apply(get_weekend)
    df_daily['season'] = df_daily['month'].apply(season)

    return df_daily

df = load_dataset()
#daily_mean = df.groupby('year')['Total'].mean()
#weekday_mean = df[df['day_of_week'] < 5].groupby('year')['Total'].mean()
#weekend_mean = df[df['weekend'] == 1].groupby('year')['Total'].mean()
year_total = df.groupby('year')['Total'].sum()
year_mean = year_total/7
#month_mean = year_total/12

left, right = st.columns(2, border=True)

#left.markdown("Daily average per year",text_alignment="center")
#left.bar_chart(daily_mean, x_label='year', y_label='average bicycle', color= "#ffaa0088", stack=False)

#right.markdown("Weekly from Monday to Friday",text_alignment="center")
#right.bar_chart(weekday_mean, x_label='year', y_label='average bicycle', color= "#ffaa0088", stack=False)

#left.markdown("Weekend",text_alignment="center")
#left.bar_chart(weekend_mean, x_label='year', y_label='average bicycle', color= "#ffaa0088", stack=False)

left.markdown("Total by Year",text_alignment="center")
left.bar_chart(year_total, x_label='year', y_label='Total bicycle', color= "#ffaa0088", stack=False)

right.markdown("Total by Year",text_alignment="center")
right.line_chart(year_total)

left.markdown("Average by Year",text_alignment="center")
left.bar_chart(year_mean, x_label='year', y_label='Total bicycle', color= "#ffaa0088", stack=False)

right.markdown("Average by Year",text_alignment="center")
right.line_chart(year_mean)

df_total = pd.DataFrame({
    'Total by year': year_total,
    'Average by Year': year_mean,
})

st.dataframe(df_total)

