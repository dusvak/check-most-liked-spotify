import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def create_spotify_oauth_manager():
    
    return SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope="user-library-read",
        cache_path=None,
        show_dialog=True,
    )
