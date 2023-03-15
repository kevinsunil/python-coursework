import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "ID"
CLIENT_KEY = "SECRET_KEY"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_KEY,
    scope="user-library-read playlist-modify-public",
    redirect_uri="http://example.com",
    show_dialog=True,
    cache_path="token.txt"
))
user_id = sp.current_user()["id"]

user_input = input("Enter the date you want to travel back to in YYYY-MM-DD format: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_input}")
content = response.text
soup = BeautifulSoup(content,"html.parser")
song_names_spans = soup.find_all("h3", class_="a-no-trucate")
song_names = [song.getText() for song in song_names_spans]
translator = str.maketrans({chr(10):'',chr(9):''})
for i in range (0,len(song_names)):
    song_names[i] = song_names[i].translate(translator)
song_uri = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{user_input.split('-')[0]}")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} skipped.")
new_playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard Top 100",public=True)
sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uri)
print(song_names)
