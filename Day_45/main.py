import requests
from bs4 import BeautifulSoup


def main() -> None:
    url: str = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
    response: str = requests.get(url=url).text

    soup = BeautifulSoup(response, "html.parser")
    article_title = soup.find_all(name="h3", class_="title")
    article_titles = [article.getText() for article in article_title][::-1]

    with open("titles.txt", "w") as file:
        for title in article_titles:
            file.write(f"{title}\n")


if __name__ == '__main__':
    main()
