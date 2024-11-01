import DataManager
import spotifyManager


def main() -> None:
    web_data: DataManager.DataManager = DataManager.DataManager()
    song_data: list = web_data.get_song_names()
    print(song_data)

    spotify: spotifyManager = spotifyManager.spotifyManager(web_data.date, song_data)
    spotify.create_playlist(f"{web_data.date} Billboard Top 100")


if __name__ == '__main__':
    main()
