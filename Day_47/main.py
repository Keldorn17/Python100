from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv  # pip install python-dotenv
import os

load_dotenv(".env")
FROM_EMAIL: str = os.getenv("FROM_EMAIL")
PASSWORD: str = os.getenv("PASSWORD")
GMAIL_SMTP: str = "smtp.gmail.com"


def send_mail(smtp_addr: str, to_addr: str, msg: str, subject: str = "") -> None:
    with smtplib.SMTP(smtp_addr) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL, to_addrs=to_addr, msg=f"Subject:{subject}\n\n{msg}")


def fetch_website(url: str, header: dict = None) -> BeautifulSoup:
    response: requests.Response = requests.get(url=url, headers=header)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')


def main() -> None:
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
        "Dnt": "1",
        "Priority": "u=1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Sec-Gpc": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
    }

    target_price: int = int(input("What is the target price you are willing to pay? "))

    website_url: str = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
    web_data: BeautifulSoup = fetch_website(website_url, header)
    price: float = float(web_data.find(class_="a-offscreen").get_text().split("$")[1])

    if price <= target_price:
        send_mail(GMAIL_SMTP, "to_addr", f"The item is below the target price at {price}",
                  "Low Price Alert")


if __name__ == '__main__':
    main()
