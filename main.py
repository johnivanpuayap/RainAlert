import requests

API_KEY = '7065e713804868f06fb225df71e10c6c'
MY_LATITUDE = 12.385330
MY_LONGITUDE = 124.330513

parameters = {
    'lat': MY_LATITUDE,
    'lon': MY_LONGITUDE,
    'appid': API_KEY,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
weather_data = response.json()['list'][0:6]

for data in weather_data:
    if data['weather'][0]['id'] < 700:
        is_raining = True
        break

if is_raining:
    print('Bring an umbrella')
