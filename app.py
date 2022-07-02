import streamlit as st
import requests

# TaxiFareModel front

st.title("New York Taxi Fare Prediction")
date = st.date_input('select date')
time = st.time_input('select the time')
pickup_longitude = st.text_input('pickup longitude', value=-73.950655)
pickup_latitude = st.text_input('pickup latitude', value=40.783282)
dropoff_latitude = st.text_input('dropoff latitude', value=40.769802)
dropoff_longitude = st.text_input('dropoff longitude', value=-73.984365)
passenger_count = st.text_input('passenger count', value=1)
date_time = str(date) + ' ' + str(time)

payload = {'pickup_datetime': date_time, 'pickup_longitude': str(pickup_longitude),
           'pickup_latitude': str(pickup_latitude), 'dropoff_longitude': dropoff_longitude,
           'dropoff_latitude': dropoff_latitude, 'passenger_count': passenger_count}

url = 'https://taxi-image-kr575za6oa-uw.a.run.app/predict?'

answer = requests.get(url, params=payload).json()

st.text(answer)
