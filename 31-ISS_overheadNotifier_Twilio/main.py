import requests

from twilio.rest import Client


account_sid = "YOUR TWILIO ACC SID"
auth_token = "YOUR TWILIO AUTH TOKEN"

#get twilio api from setting an account TWILIO

api_key = "YOUR TWILIO API KEY"

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters ={

    "lat": "29.945690",

    "lon": "78.164246",

    "appid": api_key,
    "cnt": 4,
    "units": "metric"
}

data = requests.get(OWM_ENDPOINT,params=parameters)
data.raise_for_status()

new_list = data.json()

# print(new_list['list'][0]["weather"][0]["id"])
global icon_code,img
will_rain = False
for hour_data in new_list["list"]:

    condition_code = hour_data["weather"][0]["id"]
    if (condition_code) < 700:
        will_rain = True



if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Bring An Umbrella ",
        from_="TWILIO ACCOUNT NUMBER",
        to="YOUR NUMBER"
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Its Clear",
        from_="TWILIO ACCOUNT NUMBER",
        to="YOUR NUMBER"
    )
    print(message.status)
