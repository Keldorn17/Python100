import datetime
import requests
from typing import Optional, Dict

ISS_API: str = "http://api.open-notify.org/iss-now.json"
SUNRISE_API: str = "https://api.sunrise-sunset.org/json"
LAT: float = 47.497913
LNG: float = 19.040236


def fetch_data(url: str, params: Optional[dict] = None) -> dict:
    response: requests.Response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


def is_night_time(lat: float, lng: float) -> bool:
    sunrise_params: dict = {
        "lat": lat,
        "lng": lng,
        "formatted": 0
    }

    sunrise_response: dict = fetch_data(SUNRISE_API, sunrise_params)
    sunrise: int = int(sunrise_response["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset: int = int(sunrise_response["results"]["sunset"].split("T")[1].split(":")[0])

    now: datetime.datetime = datetime.datetime.now()
    return not (sunrise < now.hour < sunset)


def is_iss_close(your_lat: float, your_lng: float) -> bool:
    iss_response: dict = fetch_data(ISS_API)

    longitude: float = float(iss_response["iss_position"]["longitude"])
    latitude: float = float(iss_response["iss_position"]["latitude"])

    return abs(latitude - your_lat) <= 5 and abs(longitude - your_lng) <= 5


def main() -> None:
    if is_night_time(LAT, LNG) and is_iss_close(LAT, LNG):
        print("Look up.")


if __name__ == '__main__':
    main()
