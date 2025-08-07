import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def create_spotify_oauth_manager():
    scope = "user-library-read"
    
    return SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope,
        cache_path=None
    )
