import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# replace with your own Spotify API credentials
client_id = 'PLACE UR CLIENT ID HERE'
client_secret = 'PLACE UR TOKEN HERE'

# create a Spotify client object with credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# define the song you want to search for
song_name = "Shape of You"
artist_name = "Ed Sheeran"

# search for the song using the Spotify API
results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track')

# extract the first song result's URL
song_url = results['tracks']['items'][0]['external_urls']['spotify']

print(f"URL for {song_name} by {artist_name}: {song_url}")