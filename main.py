##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import random
from pandas import *

# 1. Update the birthdays.csv
my_mail = "sampleudemy2@gmail.com"
password = "ayrrtrqigzcrfzvu"
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
data = read_csv("birthdays.csv")
lines = data.to_dict(orient="records")
month = now.month
day = now.day

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

for line in lines:
    if month == line["month"] and day == line["day"]:
        ch = random.randint(1, 3)
        with open(f"letter_templates/letter_{ch}.txt") as data:
            data_text = data.read()
        res = data_text.replace("[NAME]", f"{line["name"]}")

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_mail, password)
            connection.sendmail(from_addr=my_mail, to_addrs=line["email"], msg=f"Subject:Happy Birthday\n\n {res}")
