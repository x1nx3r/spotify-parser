<h1>To-do list</h1>

As i made this to supplement my discord bot the functions that i hope can be implemented are :

<h3>Implemented :</h3>

* get_songs_url = takes a songname and returns it spotify url

* get_playlist = takes a playlist name and returns it's song's as a list

* convert_to_url = the combination of get_playlist and get_songs_url in which it iterates a list and search it's song url one-by-one and putting it back in a list. 

<h3>To-do next time :</h3>

* fetch_info = fetches track info like singer, duration, and album name.

* make_playlist = creates a playlist, takes a string as a playlist name, asks creator name and store it locally. then prompt for playlist_append

* playlist_append = append a song to an existing playlist. asks for a song name, calls get_song_name and forward the output to fetch_info to make sure it's the right song, then prompt for playlist name. appends song_url to the playlist. 

* list_all_playlist = lists all existing playlist locally and creator name

* list_playlist-info = displays informations abt playlists
