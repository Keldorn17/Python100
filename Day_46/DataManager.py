from bs4 import BeautifulSoup
import requests


class DataManager:

    def __init__(self) -> None:
        self.__song_names: list = []
        self.date: str = ""
        self.__fetch_billboard()

    def __fetch_billboard(self) -> None:
        header = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        }
        self.date: str = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
        response: requests.Response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{self.date}",
                                                   headers=header)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        song_names_spans = soup.select("li ul li h3")
        self.__song_names = [song.getText().strip() for song in song_names_spans]

    def get_song_names(self) -> list[str]:
        return self.__song_names
