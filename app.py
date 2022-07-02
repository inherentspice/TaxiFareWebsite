import streamlit as st
import requests

# TaxiFareModel front

st.title("New York Taxi Fare Prediction")
st.image("https://t1.pixers.pics/img-d5043af1/canvas-prints-cartoon-monster-truck.png?H4sIAAAAAAAAA5VPy26EMAz8HZAAm7zhA_a6n4BCMLu0AaKEttv9-gZVvVTqofLB9tie8cDbluxM4Gg7KMK6TJMnmBefu9RHSsuTCqykFmWfUV8gYtnv7xRd3ENRi66qJatU21YKTdl_2Hy42vha3I8jpB4g8SYsj8yWk0vg1gQMWw3IQZppIt0KxTtBQ_D7se01xwfHJmy3Cs8oexuC_xwiZc1Eg_Xhbv9BLtnMtRj2Mdpn_Vui_HEoECtxOpv3_P1RnDP4Q-S7hrwOlysYA1KC0tDJExouV2OkVLqTgzLcMjlpJD2OrWCOke5Qjmhn1hrjmpdw-wIZxfYTgAEAAA==")
date = st.date_input('select date')
time = st.time_input('select the time')
pickup_longitude = st.text_input('pickup longitude', value=-73.950655)
pickup_latitude = st.text_input('pickup latitude', value=40.783282)
dropoff_longitude = st.text_input('dropoff longitude', value=-73.984365)
dropoff_latitude = st.text_input('dropoff latitude', value=40.769802)
passenger_count = st.text_input('passenger count', value=1)
date_time = str(date) + ' ' + str(time)

payload = {'pickup_datetime': date_time, 'pickup_longitude': str(pickup_longitude),
           'pickup_latitude': str(pickup_latitude), 'dropoff_longitude': dropoff_longitude,
           'dropoff_latitude': dropoff_latitude, 'passenger_count': passenger_count}

url = 'https://taxi-image-kr575za6oa-uw.a.run.app/predict?'

answer = requests.get(url, params=payload).json()
price = answer.get('fare')

st.text(f"Your fare will be approximately: {price}")
