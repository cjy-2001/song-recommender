import sqlite3
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

DATABASE_PATH = "music_data.sqlite"
feature_cols = ['Duration_ms', 'Explicit', 'Mode', 'Key', 'Tempo', 'Energy',
                'Danceability', 'Loudness', 'Acousticness', 'Instrumentalness',
                'Liveness', 'Speechiness', 'Valence']

# KMeans clustering
def generate_clusters(n_clusters=80):
    print("Performing clustering...")

    conn = sqlite3.connect(DATABASE_PATH)
    songs_df = pd.read_sql_query("SELECT * FROM song", conn)

    # If there are missing values, fill them with the mean of the column
    songs_df[feature_cols] = songs_df[feature_cols].fillna(songs_df[feature_cols].mean())

    # Normalize features
    normalized_df = (songs_df[feature_cols] - songs_df[feature_cols].mean()) / songs_df[feature_cols].std()

    kmeans = KMeans(n_clusters=n_clusters, n_init='auto', random_state=0).fit(normalized_df)
    songs_df['Cluster'] = kmeans.labels_

    print("Finish!")
    return songs_df[['SongId', 'Name', 'Cluster']]

def check_songs_in_database(song_list):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    songs_in_database = {}
    songs_not_in_database = []
    
    for song_name in song_list:
        cursor.execute("SELECT SongId FROM song WHERE Name = ?", (song_name,))
        result = cursor.fetchone()
        
        if result:
            songs_in_database[song_name] = result[0]
        else:
            songs_not_in_database.append(song_name)
    
    conn.close()
    return songs_in_database, songs_not_in_database

def get_artist_names(song_ids):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    artists_info = {}
    for song_id in song_ids:
        cursor.execute("""
            SELECT GROUP_CONCAT(a.Name, ', ') 
            FROM song_artist AS sa
            JOIN artist AS a ON sa.ArtistId = a.ArtistId
            WHERE sa.SongId = ?
            GROUP BY sa.SongId
        """, (song_id,))
        result = cursor.fetchone()
        artists_info[song_id] = result[0] if result else "Unknown Artist"

    conn.close()
    return artists_info

def recommend_songs_by_cluster(liked_song_names, n_recommendations = 5):
    songs_in_db, songs_not_in_db = check_songs_in_database(liked_song_names)
    all_songs_with_clusters_df = generate_clusters()
    
    # Make recommendations based on clusters
    liked_songs_df = all_songs_with_clusters_df[all_songs_with_clusters_df['SongId'].isin(songs_in_db.values())]
    liked_clusters = liked_songs_df['Cluster'].unique()
    recommended_songs_df = all_songs_with_clusters_df[all_songs_with_clusters_df['Cluster'].isin(liked_clusters)]
    
    # Exclude the songs already liked from the recommendations
    recommended_songs_df = recommended_songs_df[~recommended_songs_df['SongId'].isin(songs_in_db.values())]
    
    if recommended_songs_df.empty:
        return {}, songs_not_in_db
    
    available_recommendations = min(len(recommended_songs_df), n_recommendations)
    recommendations_df = recommended_songs_df.sample(n=available_recommendations)
    
    # Get artist names for the recommended songs
    recommended_song_ids = recommendations_df['SongId'].tolist()
    artist_names = get_artist_names(recommended_song_ids)
    
    final_recommendations = {}
    for song_id in recommended_song_ids:
        song_name = recommendations_df.loc[recommendations_df['SongId'] == song_id, 'Name'].values[0]
        final_recommendations[song_id] = {'Name': song_name, 'Artists': artist_names[song_id]}
    
    return final_recommendations, songs_not_in_db

if __name__ == '__main__':
    final_recommendations, songs_not_in_db = recommend_songs_by_cluster(["Shape of You", "Despacito", "Believer", "Harper"])
    print(f'Recommendations: {final_recommendations}') 
    print(f'Songs not in database: {songs_not_in_db}')