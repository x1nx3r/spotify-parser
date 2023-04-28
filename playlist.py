import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# replace with your own Spotify API credentials
client_id = 'PLACE UR CLIENT ID HERE'
client_secret = 'PLACE UR TOKEN HERE'

# create a Spotify client object with credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# define the playlist you want to search for
playlist_name = "chill vibes"

# search for the playlist using the Spotify API
results = sp.search(q=f'playlist:{playlist_name}', type='playlist')

# extract the first playlist result's name and URL
playlist_name = results['playlists']['items'][0]['name']
playlist_url = results['playlists']['items'][0]['external_urls']['spotify']

print(f"Playlist '{playlist_name}' URL: {playlist_url}")
