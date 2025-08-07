from collections import Counter

def analyze_top_artists(tracks):

    if not tracks:
        print("No tracks available for analysis.")
        return []
    
    print("Analyzing top artists...")
    
    artist_list = []
    for track in tracks:
        if track and track['artists']:
            for artist in track['artists']:
                artist_list.append(artist['name'])

    top_artists = Counter(artist_list).most_common(10)

    print(f'Analysis complete.')
    return top_artists

def analyze_top_genres(tracks, sp_client):

    if not tracks:
        print("No tracks available for analysis.")
        return []
    
    print("Analyzing top genres...")

    artists_ids = set()
    for track in tracks:
        if track and track['artists']:
            for artist in track['artists']:
                artists_ids.add(artist['id'])

    all_genres = []
    artist_id_list = list(artists_ids)

    for i in range(0, len(artist_id_list), 50):
        batch = artist_id_list[i:i + 50]
        try:
            artists_data = sp_client.artists(batch)
            for artist in artists_data['artists']:
                all_genres.extend(artist['genres'])
        except Exception as e:
            print(f"Error fetching artist data: {e}")

    top_genres = Counter(all_genres).most_common(10)
    
    print('Genre analysis complete.')
    
    return top_genres

