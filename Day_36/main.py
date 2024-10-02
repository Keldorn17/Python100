import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY_ALPHA_VANTAGE: str = os.getenv("API_KEY_ALPHA_VANTAGE")
NEWS_API_KEY: str = os.getenv("NEWS_API_KEY")
URL_ALPHA_VANTAGE: str = "https://www.alphavantage.co/query"
URL_NEWS: str = "https://newsapi.org/v2/everything"

STOCK: str = "TSLA"
COMPANY_NAME: str = "Tesla Inc"

ALPHA_PARAMS: dict = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_ALPHA_VANTAGE,
    "outputsize": "compact"
}


def fetch_data(url: str, params: dict = None, header: dict = None) -> dict:
    response: requests.Response = requests.get(url=url, params=params, headers=header)
    response.raise_for_status()
    return response.json()


def check_price_fluctuation(alpha_data: dict) -> float:
    data_list: list = [value for (key, value) in alpha_data["Time Series (Daily)"].items()]
    difference: float = abs(float(data_list[0]["4. close"]) - float(data_list[1]["4. close"]))
    return round((difference / float(data_list[0]["4. close"])) * 100, 2)


def get_formated_data(news_data: dict, alpha_data: dict, article_amount: int, stock_name: str) -> list[str]:
    up_or_down: str = fluctuation_direction(alpha_data)
    difference: float = check_price_fluctuation(alpha_data)
    articles: dict = news_data["articles"]
    return [f"{stock_name}: {up_or_down}{difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
            for article in articles[:article_amount]]


def fluctuation_direction(alpha_data: dict) -> str:
    data_list: list = [value for (key, value) in alpha_data["Time Series (Daily)"].items()]
    difference: float = float(data_list[0]["4. close"]) - float(data_list[1]["4. close"])
    if difference > 0:
        return "📈"
    return "📉"


def main() -> None:
    alpha_data: dict = fetch_data(URL_ALPHA_VANTAGE, ALPHA_PARAMS)
    if check_price_fluctuation(alpha_data) > 5.0:
        news_data: dict = fetch_data(URL_NEWS, {"qInTitle": COMPANY_NAME}, {"X-Api-Key": NEWS_API_KEY})
        formated_data: list = get_formated_data(news_data, alpha_data, 3, STOCK)
        for item in formated_data:
            print(item)


if __name__ == '__main__':
    main()

