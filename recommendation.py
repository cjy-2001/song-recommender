from collections import defaultdict
import sqlite3
import random
import pandas as pd
import numpy as np
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
    return songs_df

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

def get_feature_vectors(songs_df, song_ids):
    return songs_df.loc[songs_df['SongId'].isin(song_ids), feature_cols]

def allocate_recommendations(cluster_songs, total_recommendations=20):
    cluster_counts = {cluster: len(song_ids) for cluster, song_ids in cluster_songs.items()}
    total_input_songs = sum(cluster_counts.values())
    
    allocations = {cluster: (count / total_input_songs) * total_recommendations for cluster, count in cluster_counts.items()}
    rounded_allocations = {cluster: round(count) for cluster, count in allocations.items()}
    
    # Adjust allocations if necessary to ensure the total is exactly total_recommendations
    allocated_sum = sum(rounded_allocations.values())

    while allocated_sum < total_recommendations:
        most_popular_cluster = max(cluster_counts, key=cluster_counts.get)
        rounded_allocations[most_popular_cluster] += 1
        allocated_sum = sum(rounded_allocations.values())
                
    while allocated_sum > total_recommendations:
        least_popular_cluster = min(cluster_counts, key=cluster_counts.get)
        rounded_allocations[least_popular_cluster] -= 1
        allocated_sum = sum(rounded_allocations.values())

    return rounded_allocations

def get_artist_names(song_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT GROUP_CONCAT(a.Name, ', ') 
        FROM song_artist AS sa
        JOIN artist AS a ON sa.ArtistId = a.ArtistId
        WHERE sa.SongId = ?
        GROUP BY sa.SongId
    """, (song_id,))
    result = cursor.fetchone()
    artists_info = result[0] if result else "Unknown Artist"

    conn.close()
    return artists_info

def recommend_songs_by_cluster(liked_song_names, n_recommendations = 5):
    songs_in_db, songs_not_in_db = check_songs_in_database(liked_song_names)
    all_songs_with_clusters_df = generate_clusters()
    
    cluster_songs = defaultdict(list)
    for song_name, song_id in songs_in_db.items():
        cluster = all_songs_with_clusters_df.loc[all_songs_with_clusters_df['SongId'] == song_id, 'Cluster'].values[0]
        cluster_songs[cluster].append(song_id)

    cluster_vectors = {}
    for cluster, song_ids in cluster_songs.items():
        liked_songs_cluster_df = all_songs_with_clusters_df[all_songs_with_clusters_df['SongId'].isin(song_ids)]
        liked_songs_cluster_features = liked_songs_cluster_df[feature_cols]
        liked_songs_cluster_features = liked_songs_cluster_features.fillna(liked_songs_cluster_features.mean())
        mean_vector = liked_songs_cluster_features.mean().values.reshape(1, -1)
        cluster_vectors[cluster] = mean_vector

    # Exclude the songs already liked from the recommendations
    liked_clusters = cluster_songs.keys()
    candidate_songs_df = all_songs_with_clusters_df[all_songs_with_clusters_df['Cluster'].isin(liked_clusters)]
    candidate_songs_df = candidate_songs_df[~candidate_songs_df['SongId'].isin(songs_in_db.values())]
    
    if candidate_songs_df.empty:
        return {}, songs_not_in_db
    
    cluster_allocations = allocate_recommendations(cluster_songs)
    final_recommendations = {}
    for cluster, allocation in cluster_allocations.items():
        cluster_songs_df = candidate_songs_df[candidate_songs_df['Cluster'] == cluster]
        cluster_song_features = cluster_songs_df[feature_cols]
        cluster_song_features = cluster_song_features.fillna(cluster_song_features.mean())
        cluster_song_matrix = cluster_song_features.values

        similarities = cosine_similarity(cluster_vectors[cluster], cluster_song_matrix)

        top_indices = np.argsort(similarities[0])[::-1][:allocation]
        top_songs = cluster_songs_df.iloc[top_indices]

        for _, row in top_songs.iterrows():
            final_recommendations[row['SongId']] = {'Name': row['Name'], 'Artists': get_artist_names(row['SongId'])}
    
    n_recommendations = min(n_recommendations, len(final_recommendations))
    random_keys = random.sample(list(final_recommendations.keys()), n_recommendations)
    random_recommendations = {key: final_recommendations[key] for key in random_keys}

    return random_recommendations, songs_not_in_db

if __name__ == '__main__':
    final_recommendations, songs_not_in_db = recommend_songs_by_cluster(["rockstar (feat. 21 Savage)"], 5)
    print(f'Recommendations: {final_recommendations}') 
    print(f'Songs not in database: {songs_not_in_db}')