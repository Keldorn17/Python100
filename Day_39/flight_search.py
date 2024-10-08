import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")


class FlightSearch:

    def __init__(self) -> None:
        self.__token_url: str = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.__get_url: str = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.__flight_url: str = "https://test.api.amadeus.com/v2/shopping/flight-offers"
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

    def get_destination_code(self, city_name: str) -> str:
        print(f"Using this token to get destination {self.__token}")
        headers = {"Authorization": f"Bearer {self.__token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=self.__get_url,
            headers=headers,
            params=query
        )
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time) -> dict:
        headers = {"Authorization": f"Bearer {self.__token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=self.__flight_url,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
