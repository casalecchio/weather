import streamlit as st
import requests
st.title('App meteo api')

API_key ="126bd8f296de860062f6641333b1ae62"
city_name=st.text_input('inserisci la città')
if city_name:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    result = requests.get(url)
    json = result.json()
    
    country = json["sys"]['country']
    sunset1 = json["sys"]['sunset']
    wind_speed = json['wind']['speed']
    wind_deg = json['wind']['deg']

    
    
    
    
    
    
    
    st.write(country)
    st.write(sunset1)
    st.write(wind_speed)
    st.write(wind_deg)