# Stock News Notifier
Stay informed about stock market changes and relevant news with this Python script. The script fetches daily stock data from Alpha Vantage and checks for significant changes. If the percentage difference in the closing prices is less than 5%, it also retrieves top news articles related to the specified company from News API. Notifications are then sent via SMS using Twilio.

## How to Use
Obtain API Keys:
Sign up on Alpha Vantage and News API to get your API keys.

Set Environment Variables:
Create a .env file in the project directory.

Add the following variables to the file:
ALPHA_VANTAGE_API_KEY='your_alphavantage_api_key'
NEWS_API_KEY='your_news_api_key'
TWILIO_ACCOUNT_SID='your_twilio_account_sid'
TWILIO_AUTH_TOKEN='your_twilio_auth_token'

Install Dependencies:
Run the following command to install the required Python packages:
pip install requests twilio

Run the Script:
Execute the script in a Python environment.
python stock_news_notifier.py

## Features
Stock Data Retrieval: Fetches daily stock data from Alpha Vantage API.
Percentage Difference: Calculates the percentage difference in closing prices between yesterday and the day before.
News Retrieval: If the percentage difference is less than 5%, retrieves top news articles related to the specified company from News API.
Twilio Integration: Sends SMS notifications with stock information and news using Twilio.
Ensure that the API keys are correctly set in the environment variables. Stay updated on stock changes and relevant news with the Stock News Notifier!
