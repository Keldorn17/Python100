import requests
import os
from dotenv import load_dotenv  # pip install python-dotenv
from twilio.rest import Client

load_dotenv(".env")
API_URL: str = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY: str = os.getenv("API_KEY")
ACCOUNT_SID: str = os.getenv("ACCOUNT_SID")
AUTH_TOKEN: str = os.getenv("AUTH_TOKEN")
LAT: float = 46.896371
LON: float = 19.689686

WEATHER_PARAMS: dict = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4
}


def send_sms(account_sid: str, auth_token: str, to_number: str) -> None:
    client: Client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+18632261889',
        to=to_number
    )
    print(message.status)


def fetch_data(url: str, params: dict = None) -> dict:
    response: requests.Response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


def will_it_rain(weather_data: dict) -> bool:
    for condition in weather_data:
        if condition["weather"][0]["id"] < 700:
            return True
    return False


def main() -> None:
    data: dict = fetch_data(API_URL, WEATHER_PARAMS)["list"]

    if will_it_rain(data):
        print("Bring an umbrella.")
        # send_sms(ACCOUNT_SID, AUTH_TOKEN, "Number to send")


if __name__ == '__main__':
    main()
