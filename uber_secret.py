import pandas as pd
import streamlit as st
import numpy as np
import time
import datetime
# import os

# st.write(
#     "Has environment variables been set:",
#     os.environ["DATA_URL"] == st.secrets["DATA_URL"],
# )

st.set_page_config(
    page_title="Uber",
    page_icon="🚖",
    # layout="wide"
)

st.title("Uber pickups and drop off in NYC")
st.markdown("Nothing fancy, just testing **Streamlit Community Cloud** functionality with streamlit **demo** data")

DATE_COLUMN = 'date/time'
# DATA_URL = st.secrets["DATA_URL"]
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#          'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

load_status = st.warning('Wait, please. Loading all data and caching it for a quicker access later.')
data = load_data(10000)
load_status.success('All data has been loaded successfully and cached!')

# Clear values from *all* all in-memory and on-disk data caches:
if st.button("⚠️ Clear all cache and reload"):
    st.cache_data.clear()
    st.experimental_rerun()


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)


st.header("Pick a specific hour")
col1, col2 = st.columns([.3,1])

with col1:
    st.subheader("Slider")
    hour_to_filter = st.slider('Pick an hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

with col2:
    st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    st.map(filtered_data)