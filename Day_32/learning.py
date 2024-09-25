import smtplib
import datetime as dt
import random

from_email: str = "from_addr"
password: str = "app password"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=from_email, password=password)
#     connection.sendmail(from_addr=from_email, to_addrs="to_addr",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# now: dt.datetime = dt.datetime.now()
# year: int = now.year
# day_of_week: int = now.weekday()
# print(now)
# print(year)
# print(day_of_week)
#
# date_of_birth: dt.datetime = dt.datetime(year=1999, month=3, day=24, hour=23)
# print(date_of_birth)

with open("quotes.txt") as data_file:
    quotes_list: list[str] = data_file.readlines()

now: dt.datetime = dt.datetime.now()
if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email, to_addrs="to_addr",
                            msg=f"Subject:Monday Quotes\n\n{random.choice(quotes_list)}")
