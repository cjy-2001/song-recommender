from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from app.models.user import User
from app.models.song import Song
from app import db
from sqlalchemy.orm import Session

feature_cols = ['Duration_ms', 'Explicit', 'Mode', 'Key', 'Tempo', 'Energy',
                'Danceability', 'Loudness', 'Acousticness', 'Instrumentalness',
                'Liveness', 'Speechiness', 'Valence']


def update_clusters(app, n_clusters=100):
    print("Performing clustering...")
    with app.app_context():
        songs = Song.get_all_songs()
        songs_data = [song.__dict__ for song in songs]
        songs_df = pd.DataFrame(songs_data)
        songs_df[feature_cols] = songs_df[feature_cols].fillna(songs_df[feature_cols].mean())
        normalized_df = (songs_df[feature_cols] - songs_df[feature_cols].mean()) / songs_df[feature_cols].std()
        kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(normalized_df)
        songs_df['Cluster'] = kmeans.labels_

        update_data = songs_df[['SongId', 'Cluster']].to_dict(orient='records')

        session = Session(bind=db.engine)
        session.bulk_update_mappings(Song, update_data)
        session.commit()
        print("Finish!")


def recommend_songs(user_id, n_likes=5, n_recommendations=5, n_samples=100):
    user = User.find_by_id(user_id)
    liked_songs = [song.get_id() for song in user.get_liked_songs(n_likes)]
    if len(liked_songs) == 0:
        return "You have not liked any songs yet. Please like some songs to get recommendations.", None
    songs = Song.get_all_songs()
    songs_data = [song.__dict__ for song in songs]
    songs_df = pd.DataFrame(songs_data)
    songs_df = songs_df.drop('_sa_instance_state', axis=1)
    recommended_songs = recommend_songs_helper(songs_df, liked_songs, n_recommendations, n_samples)
    if len(recommended_songs) == 0:
        return "You have explored all available music, no recommendations available", None
    return "", Song.get_songs_by_ids(recommended_songs)


def recommend_songs_helper(songs_df, liked_songs, n_recommendations, n_samples):
    liked_songs_df = songs_df.loc[songs_df['SongId'].isin(liked_songs)]
    candidate_songs_df = songs_df.loc[~songs_df['SongId'].isin(liked_songs)]
    if len(candidate_songs_df) == 0:
        return []
    n_recommendations = min(n_recommendations, len(candidate_songs_df), n_samples)
    if len(candidate_songs_df) < n_samples:
        candidate_songs_df = candidate_songs_df.sample(n=n_samples, replace=True)
    else:
        candidate_songs_df = candidate_songs_df.sample(n=n_samples, replace=False)

    recommended_songs_similarity = recommend_by_similarity(liked_songs_df, candidate_songs_df, n_recommendations)
    recommended_songs_cluster = recommend_songs_by_cluster(liked_songs_df, candidate_songs_df, n_recommendations)
    print(recommended_songs_similarity)
    print(recommended_songs_cluster)
    recommended_songs = list(set(recommended_songs_similarity + recommended_songs_cluster))
    return recommended_songs


def recommend_by_similarity(liked_songs_df, candidate_songs_df, n_recommendations):
    liked_features = liked_songs_df[feature_cols]
    liked_features = liked_features.fillna(liked_features.mean())
    mean_vector = liked_features.mean().values.reshape(1, -1)
    candidate_features = candidate_songs_df[feature_cols]
    candidate_features = candidate_features.fillna(candidate_features.mean())
    song_matrix = candidate_features.values

    similarity = cosine_similarity(mean_vector, song_matrix)

    indices = np.argsort(similarity[0])[::-1][:n_recommendations]

    return candidate_songs_df.iloc[indices]['SongId'].values.tolist()


def recommend_songs_by_cluster(liked_songs_df, candidate_songs_df, n_recommendations):
    liked_clusters = liked_songs_df['Cluster'].unique()
    recommended_songs = candidate_songs_df[candidate_songs_df['Cluster'].isin(liked_clusters)]
    if len(recommended_songs) == 0:
        return []
    available_recommendations = len(recommended_songs)
    if available_recommendations < n_recommendations:
        n_recommendations = available_recommendations
    return recommended_songs.sample(n=n_recommendations)['SongId'].values.tolist()
