# Proposal for CS 558 Project: Music Recommendation System

## Introduction
The project aims to develop a music recommendation system leveraging a rich dataset of song metadata and user interactions. The system will utilize three primary recommendation techniques to deliver personalized music suggestions:

1. Content-Based Filtering
2. Collaborative Filtering
3. Rule-Based Systems

The primary focus will be on content-based filtering and rule-based systems, as the available dataset contains comprehensive song metadata, enabling effective implementation of these approaches. Content-based filtering will analyze the inherent characteristics of songs, such as genre, artist, and audio features, to recommend tracks similar to those a user has previously enjoyed. Rule-based systems will employ predefined rules and conditions to match users with suitable music recommendations based on their preferences and listening history.

While collaborative filtering is a powerful technique that leverages the collective wisdom of user communities to suggest items based on similarities between users, its implementation in this project will be limited due to the lack of extensive real-world user interaction data. However, to explore the potential of collaborative filtering, we have generated a synthetic dataset simulating user interactions. If time permits, we would like to conduct some experiments and gain insights into this approach.

The objective is to provide users with songs that align with their preferences and introduce new music that resonates with their tastes, offering a personalized and enjoyable listening experience and providing explanations for each recommendation.

## Data
We obtained our data from [Kaggle](https://www.kaggle.com/datasets/vatsalmavani/spotify-dataset/data). The dataset is a comprehensive collection obtained from Spotify and features a robust set of attributes encapsulating song characteristics. The main `song` table includes 1,706,60 records, and all the tables are housed in a SQLite database. We have preprocessed the data to ensure consistency and relevance for the recommendation algorithms. Here is a detailed description of each table and its columns:

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

We've added the `user_follow` and `user_like` tables to the original Kaggle dataset specifically for testing the collaborative filtering method. It's important to note that the data in these tables is artificial, created solely for the purpose of our experiments to approximate user interactions and preferences.

## Methodology
The project will incorporate the following methods to build the recommendation engine:

1. Content-Based Filtering:
  - This approach utilizes the intrinsic characteristics of songs, such as genre, beat, tempo, and lyrics, to recommend new tracks that share similar features with the user's preferred songs.
  - By analyzing the attributes of songs a user has previously enjoyed, the system can identify and suggest new songs that align with their established tastes.
  - Content-based filtering leverages the rich metadata available in the dataset, allowing for a comprehensive understanding of each song's musical properties and enabling accurate recommendations based on similarity.
2. Collaborative Filtering:
  - User-User Filtering: This technique recommends songs based on the preferences of users with similar listening habits.
  - By identifying users who have historically enjoyed similar songs, the system can suggest new tracks that these like-minded users have positively interacted with.
  - However, due to the limited availability of real user interaction data, the implementation of user-item filtering will be restricted in this project.
3. Rule-Based Systems:
  - This approach involves crafting predefined rules and conditions to guide song recommendations.
  - These rules can encompass various factors, such as genre preferences, artist popularity, or specific audio features.
  - By establishing a set of rules based on domain knowledge and user preferences, the system can filter and prioritize songs that satisfy these criteria.

We will mainly use content-based filtering and rule-based system for this project, because user-item filtering requires a large amount of real user data, which is hard to obtain.

## Usage
The music recommendation system will be implemented as a command-line application. Users will be prompted to enter a few song names or artists they enjoy, and they can also specify the number of recommendations they would like to receive. If time permits, we will deploy our algorithm to a web application using the Streamlit framework, offering a music recommendation system that aims to provide a seamless and personalized experience, helping users discover new music while aligning with their established preferences.

The application will then utilize the developed recommendation algorithms to generate personalized song suggestions based on the user's input and the selected recommendation technique (content-based filtering, collaborative filtering, or rule-based systems).

Additionally, users will have the option to provide more granular preferences, such as:

- Specific genres they are interested in exploring
- Audio features (e.g., tempo, energy level) they would like to prioritize
- Artist popularity or familiarity levels

By allowing users to fine-tune their preferences, the system aims to deliver highly tailored and relevant music recommendations that cater to their individual tastes and desired listening experience.

## Division of Labor:
- Jiayi Chen:
  1. Data Preprocessing: Cleansing and standardizing data for the recommendation engine.
  2. Algorithm Development: Implementing and tuning the content-based filtering algorithms.
  3. Usser interface implementation: Developing the command-line application for user interaction.

- Harper Qi:
  1. Rule-Based Logic Implementation: Developing the rule-based recommendation logic.
  2. Testing: Conducting thorough testing of the recommendation system to ensure accuracy and reliability.
  3. Explanation: Designing and implementing the explanation component, providing clear and informative justifications for each recommendation.

## Explainability:
The system will provide explanations for each song recommendation, highlighting shared attributes with liked songs (content-based), similarities with other users' preferences (collaborative filtering), or satisfied rules/conditions (rule-based).

## Annotated Bibliography: 
- K. V, S. B, U. M and V. R, "Machine Learning Model Based System Design For Music Recommendation," 2023 International Conference on System, Computation, Automation and Networking (ICSCAN), PUDUCHERRY, India, 2023, pp. 1-5, doi: 10.1109/ICSCAN58655.2023.10394917.
  - This paper explores the development of a music recommendation system through content-based filtering techniques. The authors analyze user preferences based on characteristics of previously listened to music to suggest new, appropriate tracks. The abundance of digital music and the challenge of navigating large music libraries underscore the utility of machine learning models in managing and recommending music tailored to individual tastes. This study is pertinent to the development of a music recommendation system that similarly focuses on content-based filtering. The discussion on overcoming the information overload in digital music collections by using automated systems aligns with the project's goals to enhance user experience by recommending songs that not only reflect users' past preferences but also introduce them to new music within their preferred genres and styles. The insights from this paper will guide the enhancement of content-based filtering approaches in the project, ensuring effective utilization of song characteristics such as genre, tempo, and artist details. The emphasis on practical applications in contemporary digital music services provides a valuable perspective for implementing these strategies within the project.


- B. McFee, L. Barrington and G. Lanckriet, "Learning Content Similarity for Music Recommendation," in IEEE Transactions on Audio, Speech, and Language Processing, vol. 20, no. 8, pp. 2207-2218, Oct. 2012, doi: 10.1109/TASL.2012.2199109.
  - This paper addresses the challenge of music recommendation and playlist generation for online radio within a query-by-example framework. It discusses the limitations of current collaborative filtering methods, which rely heavily on historical user data, thus hindering their performance when dealing with novel or less popular musical items. To overcome these challenges, the authors propose an innovative approach to optimize content-based similarity measures by incorporating lessons learned from collaborative filtering data. This allows the recommendation system to extend its reach to novel items effectively, achieving high accuracy while maintaining efficiency in music representation.
This study is highly relevant to the music recommendation system project, which similarly seeks to integrate content-based filtering alongside other techniques. The proposed method of enhancing content-based approaches by learning from collaborative filtering experiences aligns well with the project's goal of balancing recommendation accuracy with the ability to introduce new and diverse musical options to users. The insights from McFee and colleagues' research can directly influence the development and refinement of the project's recommendation algorithms, particularly in improving how the system handles less popular or newly added songs. This approach ensures that the system remains robust and versatile, capable of delivering personalized music experiences to a wide range of users.


- [Anonymous. "Recommendation Systems: Content-Based and Collaborative Filtering Methods."](https://github.com/ugis22/music_recommender/blob/master/content%20based%20recommedation%20system/content_based_music_recommender.ipynb)
  - This GitHub repository offers a comprehensive overview and implementation of two primary types of recommendation systems: content-based filters and collaborative filters. Content-based filters recommend items to users based on the user's past preferences, using a method that can be likened to a user-specific classification problem. This approach primarily employs keyword matching, where meaningful keywords from a user-liked item's description are used to find similar items. Specifically, the repository highlights the use of Term Frequency-Inverse Document Frequency (TF-IDF) for matching processes in song recommendations. In contrast, collaborative filters predict user preferences based on the likes and dislikes of similar users.
The repository is pertinent to the development of a music recommendation system project that employs both content-based and collaborative filtering techniques. It provides practical coding examples and theoretical insights that can enhance the understanding and implementation of these recommendation strategies. By exploring the code and methodologies shared in this repository, the project can benefit from proven practices in the field of recommendation systems, especially in handling textual data for content-based filtering. This resource is valuable for implementing efficient and effective content-based filtering processes, thereby improving the accuracy of personalized song recommendations.

- [Anonymous. "Music Recommendation System Visualization using Spotify Dataset"](https://www.kaggle.com/code/saurabhbagchi/music-recommendation-system-using-spotify-dataset)
  - This kernel presents the development of a music recommendation system using data sourced from Spotify. The author outlines the process of understanding and analyzing the dataset through various visualization techniques and exploratory data analysis (EDA). The primary goal of this EDA is to identify relevant features that can be effectively utilized to build a recommendation system. The kernel provides insights into how data visualization helps in uncovering patterns and relationships within the data that are crucial for feature selection in the recommendation engine.
This resource is particularly relevant to the music recommendation system project, as it directly deals with the use of Spotify data, similar to the dataset employed in the project. The methodologies demonstrated for data visualization and feature selection through EDA can be instrumental in refining the project's approach to developing its recommendation algorithms. By applying the techniques shared in this kernel, the project can enhance its ability to discern and utilize key musical attributes that influence user preferences, thereby improving the accuracy and personalization of the recommendations provided to users.
