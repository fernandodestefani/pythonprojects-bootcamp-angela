import os
import requests
from twilio.rest import Client

env_variables = os.environ
print(env_variables)
for key, value in env_variables.items():
    print(f'{key}: {value}')

OWM_ENDPOINT = 'link_website'
API_KEY = 'personal_password'
LAT = -23.4253
LONG = -51.9386
account_sid = 'private_account'
auth_token = 'private_token'

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
        from_='private_number',
        to='+private_number'
    )
    print(message.status)
