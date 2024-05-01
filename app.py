import streamlit as st
from recommendation import recommend_songs_by_cluster, DEFAULT_FEATURE_COLS

def main():
    st.title("🎵 Song Recommender")
    st.markdown("""
                Welcome to the song recommender! 
                
                This application allows you to discover new songs based on your favorite tracks. Simply enter the names of songs you like, and the recommender will generate personalized suggestions just for you!
                
                Key Features:

                - 📝 Enter multiple song names to get diverse recommendations
                - 🎚️ Adjust the number of recommendations using the slider
                - 🎛️ Customize your recommendations by selecting the features you care about
                - 📊 Recommendations are based on advanced clustering techniques
                - 💡 Get insights into why each song is recommended
                """)
    st.subheader("Enter exact song names (one per line):")
    liked_songs_input = st.text_area("Enter song names:", height=100)
    
    n_recommendations = st.slider("Select the number of recommendations:", min_value=1, max_value=20, value=5, step=1)
    
    feature_cols = st.multiselect("Select Features", DEFAULT_FEATURE_COLS, default=DEFAULT_FEATURE_COLS)
    
    if st.button("Recommend"):
        liked_song_names = [song.strip() for song in liked_songs_input.split("\n") if song.strip()]
        
        if len(liked_song_names) == 0:
            st.warning("Please enter at least one song name.")
        elif len(feature_cols) < 4:
            st.warning("Please select at least 4 features.")
        else:
            with st.spinner("Generating recommendations..."):
                final_recommendations, songs_not_in_db, explanations = recommend_songs_by_cluster(liked_song_names, n_recommendations, feature_cols)
            
            if final_recommendations:
                st.subheader("Song Recommendations:")
                for song_id, song_info in final_recommendations.items():
                    st.write(f"- **{song_info['Name']}** by *{song_info['Artists']}*")
                    st.caption(f"Explanation: {explanations[song_id]}")
            else:
                st.warning("No recommendations found.")
            
            if songs_not_in_db:
                st.subheader("Songs not found in the database:")
                for song_name in songs_not_in_db:
                    st.write(f"- {song_name}")
            

if __name__ == '__main__':
    main()