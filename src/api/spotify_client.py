import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def create_spotify_oauth_manager():
    scope = "user-library-read"
    
    return SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope
    )


#def create_spotify_client():
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

    if not all ([client_id, client_secret, redirect_uri]):
        print('Error: Missing environment variables. Check your .env file.')
        return None

    scope = "user-library-read"

    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        cache_path=".spotipyauthcache"
    )

    sp_client = spotipy.Spotify(auth_manager=auth_manager)

    return sp_client

#def get_liked_songs(sp_client):
    print("Fetching liked songs...")

    all_tracks = []

    results = sp_client.current_user_saved_tracks(limit=50)

    while results:
        for item in results['items']:
            all_tracks.append(item['track'])

        if results['next']:
            results = sp_client.next(results)
        else:
            results = None
    
    print(f'Total liked songs fetched: {len(all_tracks)}')
    return