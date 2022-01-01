import os 
import sys 
import json 
import spotipy
import webbrowser

from spotipy import util
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal 
#python3 app.py 'username'
#get user from your spotify account 
#user id: 92bknr9ggol2gxa98wyd4y9kk
#python3 app.py 92bknr9ggol2gxa98wyd4y9kk

#export SPOTIPY_CLIENT_ID=''
#export SPOTIPY_CLIENT_SECRET=''
#export SPOTIPY_REDIRECT_URI='https://google.com/'

username = sys.argv[1]

#Erase cache and promopt for user permission 
try:
    #token = util.prompt_for_user_token(username)
    token = util.prompt_for_user_token(username, scope="user-top-read playlist-modify-public")
except:
    os.remove(f".cache-{username}")
    #token = util.prompt_for_user_token(username)
    token = util.prompt_for_user_token(username, scope="user-top-read playlist-modify-public")

# Create our spotifyObject 
spotifyObject = spotipy.Spotify(auth=token)

#getting current user data
user = spotifyObject.current_user()

#displaying the username 
displayName = user['display_name']
followers = user['followers']['total']

#getting users top song 
topSong = spotifyObject.current_user_top_tracks(1,0,'medium_term')
print(json.dumps(topSong, sort_keys=True, indent=4))
albums = topSong['items'][0]['id']
print(albums)

#from search.py 
playlist = "spotify:playlist:02tIvMxepW2ZOWGsIw8fSX"

#adding users top song to a playlist 
#playlist_add_items(playlist_id, items, position=None)
addItem = spotifyObject.playlist_add_items(playlist, [albums], position=None)


# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
#prints out json data in a format we can read 
