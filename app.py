import streamlit as st
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
import folium
import requests

# TaxiFareModel front

st.title("New York Taxi Fare Prediction")
st.image("https://t1.pixers.pics/img-d5043af1/canvas-prints-cartoon-monster-truck.png?H4sIAAAAAAAAA5VPy26EMAz8HZAAm7zhA_a6n4BCMLu0AaKEttv9-gZVvVTqofLB9tie8cDbluxM4Gg7KMK6TJMnmBefu9RHSsuTCqykFmWfUV8gYtnv7xRd3ENRi66qJatU21YKTdl_2Hy42vha3I8jpB4g8SYsj8yWk0vg1gQMWw3IQZppIt0KxTtBQ_D7se01xwfHJmy3Cs8oexuC_xwiZc1Eg_Xhbv9BLtnMtRj2Mdpn_Vui_HEoECtxOpv3_P1RnDP4Q-S7hrwOlysYA1KC0tDJExouV2OkVLqTgzLcMjlpJD2OrWCOke5Qjmhn1hrjmpdw-wIZxfYTgAEAAA==")
date = st.date_input("select date")
time = st.time_input("select the time")
geolocator = Nominatim(user_agent="New York Taxi Fare Predictor")
start_address = st.text_input("Pickup Address", value = "Wall St")
end_address = st.text_input("Dropoff Address", value = "58 Manhattan Avenue")
location = geolocator.geocode(start_address)
end_location= geolocator.geocode(end_address)
passenger_count = st.slider('Passengers', 1, 10)


m = folium.Map(location=[location.latitude, location.longitude])
folium.Marker([location.latitude, location.longitude],
              popup='Start Location').add_to(m)
folium.Marker([end_location.latitude, end_location.longitude],
                         popup='End Location').add_to(m)
st_data = st_folium(m, width=725)
pickup_longitude = location.longitude
pickup_latitude = location.latitude
dropoff_longitude = end_location.longitude
dropoff_latitude = end_location.latitude
# passenger_count = st.text_input('passenger count', value=1)
date_time = str(date) + ' ' + str(time)

payload = {'pickup_datetime': date_time, 'pickup_longitude': pickup_longitude,
           'pickup_latitude': pickup_latitude, 'dropoff_longitude': dropoff_longitude,
           'dropoff_latitude': dropoff_latitude, 'passenger_count': str(passenger_count)}

url = 'https://taxi-image-kr575za6oa-uw.a.run.app/predict?'

def get_fare(url, payload):
    answer = requests.get(url, params=payload).json()
    price = answer.get('fare')
    st.title(f"Your fare will be approximately: {price}")

if st.button('Get fare!'):
    get_fare(url, payload)
