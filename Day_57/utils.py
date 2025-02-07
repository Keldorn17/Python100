from typing import Any
import requests


def fetch_data(url: str) -> list[dict[str, Any]] | dict[str, Any]:
    response: requests.Response = requests.get(url=url)
    response.raise_for_status()
    return response.json()
