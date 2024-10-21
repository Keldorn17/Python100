from bs4 import BeautifulSoup
import requests


def fetch_website(url: str, header: dict = None) -> str:
    response: requests.Response = requests.get(url=url, headers=header)
    response.raise_for_status()
    return response.text


def main() -> None:
    header = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    date: str = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    soup = BeautifulSoup(fetch_website(f"https://www.billboard.com/charts/hot-100/{date}", header), "html.parser")

    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]
    print(song_names)


if __name__ == '__main__':
    main()
