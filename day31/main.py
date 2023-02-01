import smtplib
import datetime as dt
import random

my_email = "mail_id"
password = "password"


def send_quote():
    with open("quotes.txt", "r") as data_file:
        data = data_file.readlines()
        quote = random.choice(data)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="kevinsunil.2001@gmail.com", msg=f"Subject: Quote\n\n {quote}")


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 2:
    send_quote()
