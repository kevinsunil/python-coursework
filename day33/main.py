import requests
import datetime as dt
import smtplib
import time

my_email = "mail_id"
password = "password"
my_latitude = 19.218330
my_longitude = 72.978088
parameters = {
    "lat": my_latitude,
    "lng": my_longitude,
    "formatted": 0
}


def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    if my_longitude - 5 <= longitude <= my_longitude + 5 and my_latitude - 5 <= latitude <= my_latitude + 5:
        check_time()


def check_time():
    response_time = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_time.raise_for_status()
    data_suntiming = response_time.json()
    sunrise_timing = float(data_suntiming['results']['sunrise'].split("T")[1].split(":")[0])
    sunset_timing = float(data_suntiming['results']['sunset'].split("T")[1].split(":")[0])
    time_now = dt.datetime.now(dt.timezone.utc).hour
    if time_now > sunset_timing or time_now < sunrise_timing:
        send_mail()


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="kevinsunil.2001@gmail.com", msg="Subject: ISS "
                                                                                          "Overhead\n\nLook up")


while True:
    time.sleep(60)
    check_position()
