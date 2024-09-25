import random
import smtplib
import datetime as dt
import pandas

FROM_EMAIL: str = "from_addr"
PASSWORD: str = "app password"
GMAIL_SMTP: str = "smtp.gmail.com"


def send_mail(smtp_addr: str, from_addr: str, to_addr: str, password: str, msg: str, subject: str = "") -> None:
    with smtplib.SMTP(smtp_addr) as connection:
        connection.starttls()
        connection.login(user=from_addr, password=password)
        connection.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=f"Subject:{subject}\n\n{msg}")


def create_custom_letter(name: str) -> str:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as data_file:
        letter: str = data_file.read()
    letter = letter.replace("[NAME]", name)
    return letter


def main() -> None:
    birthdays: pandas.DataFrame = pandas.read_csv("birthdays.csv")
    now: dt.datetime = dt.datetime.now()
    for _, birthday in birthdays.iterrows():
        if now.month == birthday["month"] and now.day == birthday["day"]:
            letter: str = create_custom_letter(birthday["name"])
            send_mail(GMAIL_SMTP, FROM_EMAIL, birthday["email"], PASSWORD, letter, "HBD")


if __name__ == '__main__':
    main()
