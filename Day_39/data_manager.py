import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")


class DataManager:

    def __init__(self):
        self.__sheety_url: str = os.getenv("SHEETY_URL")
        self.__sheety_token: str = os.getenv("SHEETY_TOKEN")
        self.destination_data: dict = {}
        self.__header = {"Authorization": f"Bearer {self.__sheety_token}"}

    def get_destination_data(self) -> dict:
        response: requests.Response = requests.get(url=self.__sheety_url, headers=self.__header)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self) -> None:
        for city in self.destination_data:
            new_data: dict = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            url: str = f"{self.__sheety_url}/{city['id']}"
            response: requests.Response = requests.put(url=url, json=new_data, headers=self.__header)
