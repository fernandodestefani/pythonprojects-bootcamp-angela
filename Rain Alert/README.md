# Weather Reminder with SMS Notifications
Stay ahead of the weather with this Python script that sends you SMS notifications if rain is expected. The script uses OpenWeatherMap API to retrieve weather information based on the provided latitude and longitude. If rain is in the forecast for the next 12 hours, you'll receive a timely reminder.

## How to Use
Obtain API Key: Sign up on OpenWeatherMap and get your personal API key.

Set Environment Variables:
Create a .env file in the project directory.
Add the following variables to the file:
OWM_ENDPOINT='https://api.openweathermap.org/data/2.5/onecall'
API_KEY='your_openweathermap_api_key'
LAT='your_latitude'
LONG='your_longitude'
account_sid='your_twilio_account_sid'
auth_token='your_twilio_auth_token'

## Features
Weather Information: Retrieves hourly weather data from OpenWeatherMap API.
Rain Notification: Checks for rain in the next 12 hours and sends an SMS if rain is expected.
Twilio Integration: Uses Twilio for sending SMS notifications securely.
Make sure to set up the environment variables correctly and have a valid Twilio account. Stay dry and informed with the Weather Reminder!

Note: This script uses OpenWeatherMap API and Twilio for weather data and SMS notifications, respectively. Ensure you comply with their terms of use.