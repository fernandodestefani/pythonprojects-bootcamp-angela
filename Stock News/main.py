import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PARAMETERS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'outputsize': 'compact',
    'datatype': 'json',
    'apikey': 'insert_apikey'
}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = 'news_api_key'
NEWS_PARAMETERS = {
    'qInTitle': COMPANY_NAME,
    'language': 'en',
    'apiKey': NEWS_API_KEY
}

account_sid = 'your_account'
auth_token = 'your_authtoken'

response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)
response.raise_for_status()
stock_data = response.json()

# yesterday_closing_price = stock_data['Time Series (Daily)']['2023-10-11']['4. close']

stock_data_summarized = stock_data['Time Series (Daily)']
dates = [date for date in stock_data_summarized]
yesterday_closing_price = float(stock_data_summarized[dates[0]]['4. close'])
day_before_yesterday_closing_price = float(stock_data_summarized[dates[1]]['4. close'])
positive_difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if positive_difference > 0:
    up_down = '🆙'
else:
    up_down = '⬇️'
percentage_difference = round((positive_difference/ yesterday_closing_price) * 100)

if abs(percentage_difference) < 5:
    response_news = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    response_news.raise_for_status()
    articles = response_news.json()['articles']
    three_articles = articles[0:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    client = Client(account_sid, auth_token)
    for n in range(0, 3):
        message = client.messages \
            .create(
            body=f"{STOCK_NAME} {up_down}{abs(percentage_difference)}%\n{formatted_articles[n]}",
            from_='+phone_number',
            to='+phone_number'
        )
        print(message.status)
