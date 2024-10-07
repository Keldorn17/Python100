from flight_search import FlightSearch
import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv(".env")

SHEETY_URL: str = os.getenv("SHEETY_URL")
SHEETY_TOKEN: str = os.getenv("SHEETY_TOKEN")
SHEETY_HEADER = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }


def get_data(url: str, params: dict = None, header: dict = None) -> dict:
    response: requests.Response = requests.get(url=url, params=params, headers=header)
    response.raise_for_status()
    return response.json()


def put_data(url: str, json: dict = None, header: dict = None) -> None:
    response: requests.Response = requests.put(url=url, json=json, headers=header)
    response.raise_for_status()


def main() -> None:
    search_engine: FlightSearch = FlightSearch()
    sheety_data: dict = get_data(SHEETY_URL, header=SHEETY_HEADER)["prices"]

    sheety_body: dict = {
        "price": {
            "iataCode": ""
        }
    }
    pprint(sheety_data)

    for row in sheety_data:
        if row["iataCode"] == "":
            sheety_body["price"]["iataCode"] = search_engine.get_iata_code(row["city"])
            print(sheety_body)
            put_data(SHEETY_URL + f"/{row["id"]}", sheety_body, SHEETY_HEADER)


if __name__ == '__main__':
    main()
