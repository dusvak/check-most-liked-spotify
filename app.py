import os
import spotipy
from flask import Flask, render_template, redirect, request, session
from dotenv import load_dotenv
from src.api.spotify_client import create_spotify_oauth_manager
from src.analysis.data_analyzer import analyze_top_artists, analyze_top_genres
from src.visualization.plot_generator import create_bar_chart

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "super-secret-key-for-dev")

def fetch_all_liked_songs(sp_client):
    all_tracks = []
    results = sp_client.current_user_saved_tracks(limit=50)
    while results:
        for item in results['items']:
            all_tracks.append(item['track'])

        if results['next']:
            results = sp_client.next(results)
        else:
            results = None    
    return all_tracks

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    sp_oauth = create_spotify_oauth_manager()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    sp_oauth = create_spotify_oauth_manager()
    code = request.args.get('code')
    session['token_info'] = sp_oauth.get_access_token(code)
    return redirect('/analyze')

@app.route('/logout')
def logout():
    session.clear()
    print("User Session Cleared")
    return redirect('/')

@app.route('/analyze')
def analyze():
    if 'token_info' not in session:
        return redirect('/')
    try:
        token_info = session.get('token_info')

        auth_manager = create_spotify_oauth_manager()

        if auth_manager.is_token_expired(token_info):
            token_info = auth_manager.refresh_access_token(token_info['refresh_token'])
            session['token_info'] = token_info

        sp = spotipy.Spotify(auth=token_info['access_token'])
        
        user_profile = sp.current_user()
        liked_songs = fetch_all_liked_songs(sp)
        top_artists = analyze_top_artists(liked_songs)
        top_genres = analyze_top_genres(liked_songs, sp)

        artist_chart = create_bar_chart(
            top_artists.copy(),
            'Top 10 Most Liked Artists',
            'Number of Liked Songs',
            'Artist'
        )

        genre_chart = create_bar_chart(
            top_genres.copy(),
            'Top 10 Most Liked Genres',
            'Number of Occurrences in Library',
            'Genre'
        )

        return render_template(
            'results.html',
            user_name=user_profile['display_name'],
            top_artists=top_artists,
            top_genres=top_genres,
            artist_chart=artist_chart,
            genre_chart=genre_chart
        )
    
    except Exception as e:
        print(f"Error during analysis: {e}")
        session.clear()
        return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
