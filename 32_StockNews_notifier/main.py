import requests
from twilio.rest import Client

MY_API_KEY = "TWILIO API KEY"

MY_NEWS_API_KEY = "YOUR NEWS API KEY - NEWSAPI.ORG"

TWILIO_SID = "YOUR SID "
TWILIO_AUTH_TOKEN = "YOUR AUTH TOKEN"


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
from datetime import date, timedelta

parameters = {
    "outputsize": "compact",
    "apikey": MY_API_KEY,
    "symbol": STOCK,
    "interval": "60min",
    "function": "TIME_SERIES_DAILY"

}

today = date.today()
day = timedelta(days=1)
yesterday = today - day
day_before_yesterday = yesterday - day

url = f"https://www.alphavantage.co/query"
r = requests.get(url, params=parameters)
data = r.json()

new_data = {
    "2024-02-07": {
        "1. open": "2887.3999",
        "2. high": "2887.3999",
        "3. low": "2840.8000",
        "4. close": "2856.8000",
        "5. volume": "115081"
    },
    "2024-02-06": {
        "1. open": "2921.2000",
        "2. high": "2940.0000",
        "3. low": "2864.0000",
        "4. close": "2877.0500",
        "5. volume": "128072"
    }
}
print(yesterday)
value_1 = float(new_data[str(day_before_yesterday)]['4. close'])
value_2 = float(new_data[str(yesterday)]['4. close'])



percentage = ((value_2 - value_1) / value_2) * 100

if percentage > 5:
    round_percentage = f"{round(percentage, 2)}📈"
else:
    round_percentage = f"{round(percentage, 2)}📉"

news_parameters = {
    "apikey": MY_NEWS_API_KEY,
    "q": COMPANY_NAME,
    "from": str(day_before_yesterday),
    "to": str(yesterday)
}

news_url = "https://newsapi.org/v2/everything"

news_request = requests.get(news_url, params=news_parameters)
description = news_request.json()
global news
for section in range(0, 5, 2):
    news = f"Tesla:{round_percentage}\n Headline: {description['articles'][section]['description']}\n Brief: {description['articles'][section]['content']}"

#
# Find your Account SID and Auth Token at twilio.com/console
#
# and set the environment variables. See http://twil.io/secure

account_sid = TWILIO_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body=f"{news}",
    from_='YOUR TWILIO NUMBER',
    to='YOUR NUMBER'
)

print(message.status )

