import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class spotifyManager:

    def __init__(self, date: str, song_names: list[str]):
        load_dotenv(".env")
        self.__SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
        self.__SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.__SPOTIFY_REDIRECT_URL = os.getenv("SPOTIFY_REDIRECT_URL")
        self.__user_id: str = ""
        self.__song_names: list[str] = song_names
        self.__song_uris: list[str] = []
        self.__date: str = date
        self.__sp: spotipy.Spotify
        self.__authentication()

    def __authentication(self) -> None:
        scope = "playlist-modify-private"

        self.__sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                              client_id=self.__SPOTIFY_CLIENT_ID,
                                                              client_secret=self.__SPOTIFY_CLIENT_SECRET,
                                                              redirect_uri=self.__SPOTIFY_REDIRECT_URL,
                                                              cache_path=".cache"))
        self.__user_id = self.__sp.current_user()["id"]

    def __search_songs(self):
        year: str = self.__date.strip("-")[0]
        for song in self.__song_names:
            result = self.__sp.search(q=f"track:{song} year:{year}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.__song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped")

    def create_playlist(self, playlist_name: str) -> None:
        self.__search_songs()
        playlist = self.__sp.user_playlist_create(user=self.__user_id, name=playlist_name, public=False)
        print(playlist)
        self.__sp.playlist_add_items(playlist_id=playlist["id"], items=self.__song_uris)

