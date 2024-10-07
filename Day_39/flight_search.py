import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")


class FlightSearch:

    def __init__(self) -> None:
        self.__token_url: str = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.__get_url: str = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.__api_key: str = os.getenv("AMADEUS_KEY")
        self.__api_secret: str = os.getenv("AMADEUS_SECRET")
        self.__token: str = self.__get_new_token()

    def __get_new_token(self) -> str:
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.__api_key,
            'client_secret': self.__api_secret
        }
        response: requests.Response = requests.post(url=self.__token_url, headers=header, data=body)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_iata_code(self, city_name: str) -> str:
        header: dict = {
            'Authorization': f"Bearer {self.__token}"
        }
        response: requests.Response = requests.get(url=self.__get_url, params={"keyword": city_name}, headers=header)
        response.raise_for_status()
        return response.json()["data"][0]["iataCode"]
