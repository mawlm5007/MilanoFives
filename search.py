#used to find the playlist id of the party throwers playlist 

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
#python3 search.py 92bknr9ggol2gxa98wyd4y9kk
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


#getting users playlist information 
#current_user_playlists(limit=50, offset=0)
userPlaylists = spotifyObject.current_user_playlists(50, 0)

print(json.dumps(userPlaylists, sort_keys=True, indent=4))

#after running we see that the playlist we want is
#Milano5Party and the uri for the playlist is "id": "02tIvMxepW2ZOWGsIw8fSX"


# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
#prints out json data in a format we can read 