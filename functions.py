import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'PLACE UR CLIENT ID HERE'
client_secret = 'PLACE UR TOKEN HERE'

# create a Spotify client object with credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_url(song_name):
    # search for the song using the Spotify API
    results = sp.search(q=f'track:{song_name}', type='track')

    # extract the first song result's URL
    song_url = results['tracks']['items'][0]['external_urls']['spotify']

    return song_url

def get_playlist_songs(playlist_name):
    # search for the playlist using the Spotify API
    results = sp.search(q=f'playlist:{playlist_name}', type='playlist')

    # extract the first playlist result's ID
    playlist_id = results['playlists']['items'][0]['id']

    # get the tracks in the playlist using the Spotify API
    tracks = sp.playlist_tracks(playlist_id, fields='items(track(name))')

    # extract the names of the songs in the playlist, in order
    song_names = [track['track']['name'] for track in tracks['items']]

    # return the list of song names
    return song_names

def convert_to_url(array):
    urllist = []
    for song_name in array:
        song_url = get_song_url(song_name)
        urllist.append(song_url)
    return urllist



