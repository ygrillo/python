import streamlit as st
import pandas as pd
import numpy as np

st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")
df_streamlit = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]})

df_streamlit

# list = np.array('1', '2', '3')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [39.76, -3.4],
    columns=['lat', 'lon'])

st.map(map_data)

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df_streamlit['first column'])

'You selected:', option



if st.checkbox('Exibir'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# Add a placeholder
#latest_iteration = st.empty()
#bar = st.progress(0)

#for i in range(100):
  # Update the progress bar with each iteration.
  #latest_iteration.text(f'Iteration {i+1}')
  #bar.progress(i + 1)
  #time.sleep(0.1)

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(data)

#st.subheader('Number of pickups by hour')
# hist_values = np.histogram(
#    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
# st.bar_chart(hist_values)

# st.subheader('Map of all pickups')
# st.map(data)
