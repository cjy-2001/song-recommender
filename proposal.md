# Proposal for CS 558 Project: Music Recommendation System

## Introduction
The project aims to develop a music recommendation system leveraging a rich dataset of user interactions and song metadata. The system will utilize three primary recommendation techniques to deliver personalized music suggestions:

1. Content-Based Filtering
2. Collaborative Filtering
3. Rule-Based Systems

The primary focus will be on content-based filtering and rule-based systems, as the available dataset contains comprehensive song metadata and user interaction data, enabling effective implementation of these approaches. Content-based filtering will analyze the inherent characteristics of songs, such as genre, artist, and audio features, to recommend tracks similar to those a user has previously enjoyed. Rule-based systems will employ predefined rules and conditions to match users with suitable music recommendations based on their preferences and listening history.

While collaborative filtering is a powerful technique that leverages the collective wisdom of user communities to suggest items based on similarities between users, its implementation in this project will be limited due to the lack of extensive real-world user interaction data. However, to explore the potential of collaborative filtering, we have generated a synthetic dataset simulating user interactions, allowing us to conduct experiments and gain insights into this approach.

The objective is to provide users with songs that align with their preferences and introduce new music that resonates with their tastes, offering a personalized and enjoyable listening experience.

## Data
We obtained our data from [Kaggle](https://www.kaggle.com/datasets/vatsalmavani/spotify-dataset/data). The dataset is a comprehensive collection obtained from Spotify and features a robust set of attributes encapsulating song characteristics. The main `song` table includes 1,706,60 records, and all the tables are housed in a SQLite database. The data has been preprocessed to ensure consistency and relevance for the recommendation algorithms. Here is a detailed description of each table and its columns:

1. song
  - `SongId`: Unique identifier for individual songs.
  - Attributes like `Name`, `Duration_ms` (duration in milliseconds), `Explicit`, `Mode`, `Key`, `Tempo`, `Energy`, and several others that define the acoustic characteristics of a song.
  - As the central table, it encapsulates extensive details about each track, enabling both content-based and collaborative filtering techniques.

2. artist
  - `ArtistId`: Unique identifier for each artist.
  - `Name`: The name of the artist.
  - This table catalogs artists, serving as a key reference for the song_artist relation and providing an artist-centric perspective to recommendations.

3. song_artist
  - `SongId`: Foreign key associated with the song table.
  - `ArtistId`: Foreign key linked to the artist table.
  - This relationship table associates songs with their respective artists, which is vital for understanding user preferences and artist popularity.

4. genre
  - `GenreId`: Unique identifier for each genre.
  - `Name`: The name of the genre.
  - The genre table is essential for categorizing songs, a critical factor in content-based filtering where a user's genre preferences significantly influence song suggestions.

5. song_genre
  - `SongId`: Foreign key connecting to the song table.
  - `GenreId`: Foreign key relating to the genre table.
  - This table connects songs to their genres, laying the groundwork for genre-based recommendations and analyses.

6. user_follow
  - `ArtistId1`: The ID of the user being followed.
  - `ArtistId2`: The ID of the user being followed by another user.
  - This table simulates user following relationships to test collaborative filtering approaches.

7. user_like
  - `SongId`: Unique identifier representing the song.
  - `ArtistId`: The ID of the user of the liked song.
  - This table mirrors user interactions with songs, reflecting likes, which are instrumental for user-item collaborative filtering.

We've included the `user_follow` and `user_like` tables in our dataset specifically for testing the collaborative filtering method. It's important to note that the data in these tables is artificial, created solely for the purpose of our experiments to approximate user interactions and preferences.

## Methodology
The project will incorporate the following methods to build the recommendation engine:

1. Collaborative Filtering:
   - User-Item Filtering: Recommendations based on users with similar listening habits.
   - Item-Item Filtering: Suggesting songs akin to the user's favorite tracks.
2. Content-Based Filtering:
   - Using song features (genre, beat, tempo, lyrics) to recommend new songs with matching characteristics.
3. Rule-Based Systems:
    - Predefined rules such as genre preferences or artist popularity will guide the recommendation of songs.

## Usage
The music recommendation system will be implemented as a user-friendly web application using the Streamlit framework. Users will be prompted to enter a few song names or artists they enjoy, and they can also specify the number of recommendations they would like to receive.

The application will then utilize the developed recommendation algorithms to generate personalized song suggestions based on the user's input and the selected recommendation technique (content-based filtering, collaborative filtering, or rule-based systems).

Additionally, users will have the option to provide more granular preferences, such as:

- Specific genres they are interested in exploring
- Audio features (e.g., tempo, energy level) they would like to prioritize
- Artist popularity or familiarity levels

By allowing users to fine-tune their preferences, the system aims to deliver highly tailored and relevant music recommendations that cater to their individual tastes and desired listening experience. The user interface will present the recommended songs in an intuitive and visually appealing manner, displaying relevant information such as song titles and artists.

Through this interactive and user-friendly interface, the music recommendation system aims to provide a seamless and personalized experience, helping users discover new music while aligning with their established preferences.

## Division of Labor:
- Jiayi Chen:
  1. Data Preprocessing: Cleansing and standardizing data for the recommendation engine.
  2. Algorithm Development: Implementing and tuning the collaborative and content-based filtering algorithms.

- Harper Qi:
  1. Rule-Based Logic Implementation: Developing the rule-based recommendation logic.
  2. Testing
  3. Explanation

## Explainability:
The system will provide explanations for each song recommendation, highlighting shared attributes with liked songs (content-based), similarities with other users' preferences (collaborative filtering), or satisfied rules/conditions (rule-based).

## Technical Specifications:
Developed in Python using Streamlit for the interactive web application. An annotated bibliography covering recommendation methodologies, music domain applications, and user interaction studies will be included. The system will be modular, extensible, and designed to run in the designated environment with proper documentation.
