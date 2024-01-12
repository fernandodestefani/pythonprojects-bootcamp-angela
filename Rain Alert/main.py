import os
import requests
from twilio.rest import Client

env_variables = os.environ
print(env_variables)
for key, value in env_variables.items():
    print(f'{key}: {value}')

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.8/onecall'
API_KEY = '61f57c1a6842056345e57cdfa44861b8'
LAT = -23.4253
LONG = -51.9386
account_sid = 'AC634e41741f89a0c6f08d997e22f58fe1'
auth_token = '35a554423f79cbd05efc4e8a48d5c2bb'

weather_params = {
    "lat": LAT,
    'lon': LONG,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# weather_id = weather_data['hourly'][0]['weather'][0]['id']

will_rain = False

weather_slice = weather_data['hourly'][:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its gonna rain today. Remember to bring an ☂️",
        from_='+12564884881',
        to='+5584987590482'
    )
    print(message.status)
