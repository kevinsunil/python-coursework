# Extra Hard Starting Project
import smtplib
import random
import datetime as dt
import pandas

birthday_list = []
letter_list = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
my_email = "mail_id"
password = "password"


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
def check_birthday():
    global birthday_list
    now = dt.datetime.now()
    month = now.month
    day = now.day
    data_file = pandas.read_csv('birthdays.csv')
    for index, rows in data_file.iterrows():
        if rows["month"] == month and rows["day"] == day:
            birthday = []
            birthday.append(rows["name"])
            birthday.append(rows["email"])
            birthday_list.append(birthday)
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
    # name from birthdays.csv
    for person in birthday_list:
        with open(f"{random.choice(letter_list)}", "r") as letter:
            data = letter.read()
            data = data.replace("[NAME]", person[0])
            send_mail(person[1], data)


# 4. Send the letter generated in step 3 to that person's email address.
def send_mail(email, msg):
    mail_id = email
    message = msg
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=f"{mail_id}", msg=f"Subject: Happy Birthday\n\n {message}")


check_birthday()
