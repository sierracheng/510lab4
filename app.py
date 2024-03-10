import datetime
import pytz
import streamlit as st
import time

def get_time_in_timezone(timezone):
    tz = pytz.timezone(timezone)
    now = datetime.datetime.now(tz)
    return now.strftime('%Y-%m-%d %H:%M:%S')

# List of time zones you want to display
timezones = {
    'UTC': 'UTC',
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Berlin': 'Europe/Berlin',
    'Tokyo': 'Asia/Tokyo',
    'Sydney': 'Australia/Sydney',
}

st.title('World Clock')

placeholder = st.empty()

while True:
    with placeholder.container():
        st.header('Current Time in Various Time Zones')
        for city, tz in timezones.items():
            st.write(f"{city}: {get_time_in_timezone(tz)}")
    time.sleep(1)
