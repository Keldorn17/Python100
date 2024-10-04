import requests
from datetime import datetime

TOKEN: str = "YoWhatsGood69"
USERNAME: str = "pythontest17"
PIXELA_ENDPOINT: str = "https://pixe.la/v1/users"  # https://pixe.la/@pythontest17
GRAPH_ID: str = "graph1"
USER_PARAMS: dict = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
GRAPH_ENDPOINT: str = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"  # https://pixe.la/v1/users/pythontest17/graphs/graph1.html
GRAPH_CONFIG: dict = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}
HEADERS: dict = {
    "X-USER-TOKEN": TOKEN
}
PIXEL_CREATION_ENDPOINT: str = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
TODAY: str = datetime.now().strftime("%Y%m%d")
PIXEL_DATA: dict = {
    "date": TODAY,
    "quantity": input("How many kilometers did you cycle today? ")
}
UPDATE_ENDPOINT: str = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
NEW_PIXEL_DATA: dict = {
    "quantity": "4.5"
}
DELETE_ENDPOINT: str = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"


def main() -> None:
    # # Create User
    # response: requests.Response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
    # print(response.text)

    # # Create Graph
    # response: requests.Response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)
    # print(response.text)

    # # Create Pixel
    # response: requests.Response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=PIXEL_DATA, headers=HEADERS)
    # print(response.text)

    # # Update Pixel
    # response: requests.Response = requests.put(url=UPDATE_ENDPOINT, json=NEW_PIXEL_DATA, headers=HEADERS)
    # print(response.text)

    # Delete Pixel
    response: requests.Response = requests.delete(url=DELETE_ENDPOINT, headers=HEADERS)
    print(response.text)


if __name__ == '__main__':
    main()
