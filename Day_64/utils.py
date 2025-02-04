from typing import Any, Optional
import requests


def fetch_data(url: str, headers: Optional[dict] = None, params: Optional[dict] = None) \
        -> list[dict[str, Any]] | dict[str, Any]:
    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
