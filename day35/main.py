import os
import requests
from twilio.rest import Client
API_KEY = "MY_API_KEY"
my_latitude = 19.218330
my_longitude = 72.978088
new_lat = -13.5666667
new_long = -67.083333
# twilio details
account_sid = "MY_ACCOUNT_SSID"
account_auth = "MY_AUTH_TOKEN"

parameters = {
    "lat": new_lat,
    "lon": new_long,
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
data_list = data["list"]
will_rain = False
for i in range(0, 12):
    if data_list[i]['weather'][0]['id'] < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid,account_auth)
    message = client.messages.create(
        body="Going to rain today bring umbrella",
        from_='MY_TWILIO_PHONE',
        to='RECIEVER_PHONE'
    )

