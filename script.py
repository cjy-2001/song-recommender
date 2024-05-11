import argparse

from recommendation import recommend_songs_by_cluster

DEFAULT_FEATURE_COLS = ['Duration_ms', 'Explicit', 'Mode', 'Key', 'Tempo', 'Energy',
                'Danceability', 'Loudness', 'Acousticness', 'Instrumentalness',
                'Liveness', 'Speechiness', 'Valence']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recommend songs based on liked songs.')
    parser.add_argument('-l', '--liked_songs', nargs='+', required=True, help='List of liked song names')
    parser.add_argument('-n', '--num_recommendations', type=int, default=5, help='Number of song recommendations (default: 5)')
    parser.add_argument('-f', '--feature_cols', nargs='+', default=DEFAULT_FEATURE_COLS, help='List of feature columns (default: DEFAULT_FEATURE_COLS)')
    args = parser.parse_args()

    liked_song_names = args.liked_songs
    n_recommendations = args.num_recommendations
    feature_cols = args.feature_cols

    # Error handling for the number of recommendations
    if n_recommendations < 1 or n_recommendations > 20:
        parser.error("Number of recommendations must be between 1 and 20.")

    # Error handling for the number of feature columns
    if len(feature_cols) < 4:
        parser.error("At least 3 feature columns must be provided.")

    # Error handling for invalid feature columns
    invalid_features = set(feature_cols) - set(DEFAULT_FEATURE_COLS)
    if invalid_features:
        parser.error(f"Invalid feature column(s): {', '.join(invalid_features)}. Available features: {', '.join(DEFAULT_FEATURE_COLS)}")

    final_recommendations, songs_not_in_db, explanations = recommend_songs_by_cluster(liked_song_names, n_recommendations, feature_cols)
    print(f'Recommendations: {final_recommendations}')
    print(f'Explanations: {explanations}')
    print(f'Songs not in database: {songs_not_in_db}')