import requests
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv(".env")
APP_ID: str = os.getenv("APP_ID")
API_KEY: str = os.getenv("API_KEY")
API_URL: str = os.getenv("API_URL")
SHEETY_URL: str = os.getenv("SHEETY_URL")
BEARER_TOKEN: str = os.getenv("BEARER_TOKEN")
GENDER: str = "male"
WEIGHT_KG: int = 80
HEIGHT_CM: int = 180
AGE: int = 21

NUTRIENTS_HEADER: dict = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


def post_data(url: str, json: dict, headers: dict = None) -> dict:
    response: requests.Response = requests.post(url=url, json=json, headers=headers)
    response.raise_for_status()
    return response.json()


def main() -> None:
    parameters = {
        "query": input("Tell me which exercise you did: "),
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    response: dict = post_data(API_URL, parameters, NUTRIENTS_HEADER)

    today_date: str = datetime.now().strftime("%m/%d/%Y")
    now_time: str = datetime.now().strftime("%X")

    sheet_inputs = None
    for exercise in response["exercises"]:
        sheet_inputs = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

    bearer_headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    sheet_response = requests.post(SHEETY_URL, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)


if __name__ == '__main__':
    main()
