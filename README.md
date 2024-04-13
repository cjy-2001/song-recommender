# CS 558 Music Recommendation System

This project aims to develop a music recommendation system that provides personalized song suggestions based on a user's provided songs. The system utilizes content-based filtering and rule-based approaches to generate recommendations.

## Introduction
The Music Recommendation System is a powerful tool designed to help users discover new songs that align with their music preferences. By analyzing the characteristics of a user's liked songs, such as genre, artist, and audio features, the system generates personalized recommendations tailored to their unique tastes.

The system employs advanced algorithms and data analysis techniques to identify patterns and similarities among songs, enabling it to suggest tracks that the user is likely to enjoy. It goes beyond simple popularity-based recommendations by considering factors like genre preferences and specific audio features that contribute to the user's listening experience.

Another compelling aspect of the Music Recommendation System is its ability to provide explanations for each recommendation. Rather than presenting a list of songs without context, the system offers insights into why a particular song is being suggested. It highlights the shared attributes between the recommended song and the user's liked songs, such as similar genres, artists, or audio features. This transparency not only enhances the user's trust in the recommendations but also fosters a deeper understanding and appreciation of their musical preferences.

## Features
- Content-based filtering:
    - Utilizes the inherent characteristics of songs, such as genre, artist, and audio features, to recommend songs similar to the user's liked songs.
    - Employs clustering techniques to group songs based on their musical attributes, allowing for more targeted recommendations.
    - Calculates the similarity between songs using cosine similarity, ensuring that the recommended songs share meaningful connections with the user's preferences.

- Rule-based approach:
    - Incorporates predefined rules and conditions to guide music recommendations, complementing the content-based filtering process.
    - Considers factors such as genre preferences and specific audio features to refine the recommendations.
    - Allows for customizable rules based on domain knowledge and user feedback, enabling fine-tuning of the recommendation process.

- Personalized recommendations:
  - Generates song suggestions that are tailored to each user's unique musical taste.
  - Allows users to specify the number of recommendations they want to receive and the features to consider in the recommendation process.

- Explanation of recommendations:
  - Provides clear and informative explanations for each recommended song, offering insights into why a particular song is being suggested.
  - Highlights the shared attributes between the recommended song and the user's liked songs, such as similar genres, artists, or audio features.

The Music Recommendation System combines the power of content-based filtering, rule-based approaches, personalization, and explanations to deliver a comprehensive and engaging music discovery experience. By leveraging these features, the system aims to help users explore new music, rediscover old favorites, and enhance their overall satisfaction with the music streaming platform.

## Installation
1. Clone the repository:
   
```bash
git clone https://github.com/cjy-2001/song-recommender.git
```

2. Install the required dependencies:
   
```bash
pip install sqlite3, pandas, sklearn, argparse
```

3. Ensure you have a SQLite database file named music_data.sqlite containing the necessary music data.

## Usage
To run the Music Recommendation System, use the following command:

```bash
python script.py -l <liked_songs> [-n <num_recommendations>] [-f <feature_cols>]
```

- `liked_songs`: A list of song names that the user likes (required)
- `num_recommendations`: The number of song recommendations to generate (optional, default: 5)
- `feature_cols`: A list of feature columns to consider for recommendations (optional, default: predefined list)

Example:

```bash
python script.py -l "Shape of You" "Believer" "Havana" -n 10
```

## Methodology
The Music Recommendation System employs the following methods:

1. Content-Based Filtering:
   - Analyzes the inherent characteristics of songs, such as genre, artist, and audio features
   - Recommends songs that share similar features with the user's liked songs

2. Rule-Based Systems:
   - Utilizes predefined rules and conditions to guide song recommendations
   - Considers factors like genre preferences, artist popularity, and specific audio features

## Explanation of Recommendations
The Music Recommendation System provides explanations for each song recommendation. It highlights the shared attributes between the recommended song and the user's liked songs, such as similar genres, artists, or audio features. This transparency helps users understand why a particular song is being recommended to them.

## Sample Output

## Contributors
- Jiayi Chen:
  1. Data Preprocessing: Cleansing and standardizing data for the recommendation engine.
  2. Algorithm Development: Implementing and tuning the content-based filtering algorithms.
  3. User Interface Implementation: Developing the command-line application for user interaction.

- Harper Qi:
  1. Rule-Based Logic Implementation: Developing the rule-based recommendation logic.
  2. Testing: Conducting thorough testing of the recommendation system to ensure accuracy and reliability.
  3. Explanation: Designing and implementing the explanation component, providing clear and informative justifications for each recommendation.

## Outlook

The Music Recommendation System has shown promising results, but there are several areas for improvement and further exploration:

1. Handling Duplicate Song Names:
The algorithm may sometimes recommend the same song multiple times due to the presence of duplicate song entries in the database with different release years. While this indicates that the algorithm is functioning correctly, it can be enhanced to handle such duplicates more effectively.

2. Case Sensitivity:
Currently, the system treats capitalized and non-capitalized song names as different entities. To improve the user experience, the song names in the database can be converted to lowercase before processing, ensuring consistent matching regardless of capitalization.

3. Expanding Rule-Based Approaches:
The current implementation primarily relies on genre-based rules for recommendations. Incorporating additional rules based on artist preferences and album information can further refine the recommendations and provide more diverse suggestions.

## Annotated Bibliography: 
- K. V, S. B, U. M and V. R, "Machine Learning Model Based System Design For Music Recommendation," 2023 International Conference on System, Computation, Automation and Networking (ICSCAN), PUDUCHERRY, India, 2023, pp. 1-5, doi: 10.1109/ICSCAN58655.2023.10394917.
  - This paper explores the development of a music recommendation system through content-based filtering techniques. The authors analyze user preferences based on characteristics of previously listened to music to suggest new, appropriate tracks. The abundance of digital music and the challenge of navigating large music libraries underscore the utility of machine learning models in managing and recommending music tailored to individual tastes. This study is pertinent to the development of a music recommendation system that similarly focuses on content-based filtering. The discussion on overcoming the information overload in digital music collections by using automated systems aligns with the project's goals to enhance user experience by recommending songs that not only reflect users' past preferences but also introduce them to new music within their preferred genres and styles. The insights from this paper will guide the enhancement of content-based filtering approaches in the project, ensuring effective utilization of song characteristics such as genre, tempo, and artist details. The emphasis on practical applications in contemporary digital music services provides a valuable perspective for implementing these strategies within the project.


- B. McFee, L. Barrington and G. Lanckriet, "Learning Content Similarity for Music Recommendation," in IEEE Transactions on Audio, Speech, and Language Processing, vol. 20, no. 8, pp. 2207-2218, Oct. 2012, doi: 10.1109/TASL.2012.2199109.
  - This paper addresses the challenge of music recommendation and playlist generation for online radio within a query-by-example framework. It discusses the limitations of current collaborative filtering methods, which rely heavily on historical user data, thus hindering their performance when dealing with novel or less popular musical items. To overcome these challenges, the authors propose an innovative approach to optimize content-based similarity measures by incorporating lessons learned from collaborative filtering data. This allows the recommendation system to extend its reach to novel items effectively, achieving high accuracy while maintaining efficiency in music representation. This study is highly relevant to the music recommendation system project, which similarly seeks to integrate content-based filtering alongside other techniques. The proposed method of enhancing content-based approaches by learning from collaborative filtering experiences aligns well with the project's goal of balancing recommendation accuracy with the ability to introduce new and diverse musical options to users. The insights from McFee and colleagues' research can directly influence the development and refinement of the project's recommendation algorithms, particularly in improving how the system handles less popular or newly added songs. This approach ensures that the system remains robust and versatile, capable of delivering personalized music experiences to a wide range of users.


- [Anonymous. "Recommendation Systems: Content-Based and Collaborative Filtering Methods."](https://github.com/ugis22/music_recommender/blob/master/content%20based%20recommedation%20system/content_based_music_recommender.ipynb)
  - This GitHub repository offers a comprehensive overview and implementation of two primary types of recommendation systems: content-based filters and collaborative filters. Content-based filters recommend items to users based on the user's past preferences, using a method that can be likened to a user-specific classification problem. This approach primarily employs keyword matching, where meaningful keywords from a user-liked item's description are used to find similar items. Specifically, the repository highlights the use of Term Frequency-Inverse Document Frequency (TF-IDF) for matching processes in song recommendations. In contrast, collaborative filters predict user preferences based on the likes and dislikes of similar users.
  - The repository is pertinent to the development of a music recommendation system project that employs both content-based and collaborative filtering techniques. It provides practical coding examples and theoretical insights that can enhance the understanding and implementation of these recommendation strategies. By exploring the code and methodologies shared in this repository, the project can benefit from proven practices in the field of recommendation systems, especially in handling textual data for content-based filtering. This resource is valuable for implementing efficient and effective content-based filtering processes, thereby improving the accuracy of personalized song recommendations.

- [Anonymous. "Music Recommendation System Visualization using Spotify Dataset"](https://www.kaggle.com/code/saurabhbagchi/music-recommendation-system-using-spotify-dataset)
  - This kernel presents the development of a music recommendation system using data sourced from Spotify. The author outlines the process of understanding and analyzing the dataset through various visualization techniques and exploratory data analysis (EDA). The primary goal of this EDA is to identify relevant features that can be effectively utilized to build a recommendation system. The kernel provides insights into how data visualization helps in uncovering patterns and relationships within the data that are crucial for feature selection in the recommendation engine.
  - This resource is particularly relevant to the music recommendation system project, as it directly deals with the use of Spotify data, similar to the dataset employed in the project. The methodologies demonstrated for data visualization and feature selection through EDA can be instrumental in refining the project's approach to developing its recommendation algorithms. By applying the techniques shared in this kernel, the project can enhance its ability to discern and utilize key musical attributes that influence user preferences, thereby improving the accuracy and personalization of the recommendations provided to users.
