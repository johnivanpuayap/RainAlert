import requests
import os
from twilio.rest import Client

# DATA
MY_LATITUDE = 12.385330
MY_LONGITUDE = 124.330513
MY_PHONE_NUMBER = '+639561886073'


# LOAD API KEYS
OPENWEATHER_API_KEY = os.environ['OPENWEATHER_API_KEY']
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_PHONE_NUMBER = '+14706135180'

parameters = {
    'lat': MY_LATITUDE,
    'lon': MY_LONGITUDE,
    'appid': OPENWEATHER_API_KEY,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
weather_data = response.json()['list'][0:6]

# Check the Weather
for data in weather_data:
    if data['weather'][0]['id'] < 700:
        will_rain = True
        break

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

if will_rain:
    # Send an SMS
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    )
    print(message.sid)