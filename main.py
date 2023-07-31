import requests
import os
from twilio.rest import Client

API_KEY = os.environ['OPENWEATHER_API_KEY']
MY_LATITUDE = 12.385330
MY_LONGITUDE = 124.330513
TRIAL_NUMBER = +14706135180

parameters = {
    'lat': MY_LATITUDE,
    'lon': MY_LONGITUDE,
    'appid': API_KEY,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
weather_data = response.json()['list'][0:6]

# Check the Weather
for data in weather_data:
    if data['weather'][0]['id'] < 700:
        will_rain = True
        break

if will_rain:

    # Send an SMS
    print('Bring an umbrella')
