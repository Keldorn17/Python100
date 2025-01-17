import requests
from bs4 import BeautifulSoup


class ScrapeData:

    def __init__(self) -> None:
        self.__listing_data: list[dict] = []
        self.__request_data()

    def get_listing_data(self) -> list[dict]:
        return self.__listing_data

    def __request_data(self) -> None:
        website: str = "https://appbrewery.github.io/Zillow-Clone/"
        response: requests.Response = requests.get(url=website)
        response.raise_for_status()

        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

        price_list_spans = soup.select("[data-test='property-card-price']")
        price_list: list[str] = [price.getText()[:6] for price in price_list_spans]

        link_list_spans = soup.select("[data-test='property-card-link']")
        link_list: list[str] = [link.get("href") for i, link in enumerate(link_list_spans) if i % 2 == 0]
        address_list: list[str] = [link.getText().strip() for link in link_list_spans if link.getText().strip() != ""]

        for i in range(len(price_list)):
            self.__listing_data.append({
                "Address": address_list[i],
                "Price": price_list[i],
                "Link": link_list[i]
            })
