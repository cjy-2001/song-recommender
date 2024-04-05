# Proposal for CS 558 Project: Music Recommendation System

## Introduction
The project aims to develop 'Harmonize', a music recommendation system leveraging a rich dataset of user interactions and song metadata. The system will use three primary recommendation techniques to deliver personalized music suggestions:

1. Collaborative Filtering (both User-Item and Item-Item)
2. Content-Based Filtering
3. Rule-Based Systems

The objective is to provide users with songs that align with their historical preferences and introduce new music that resonates with their tastes.

## Dataset Description
The dataset includes user profiles, song details, listening history, and interactions (likes, follows). It comprises information about user activities, song genres, artists, and audio features essential for the recommendation algorithms.

## Methodology
The project will incorporate the following methods to build the recommendation engine:

1. Collaborative Filtering:
   - User-Item Filtering: Recommendations based on users with similar listening habits.
   - Item-Item Filtering: Suggesting songs akin to the user's favorite tracks.
2. Content-Based Filtering:
   - Using song features (genre, beat, tempo, lyrics) to recommend new songs with matching characteristics.
3. Rule-Based Systems:
    - Predefined rules such as genre preferences or artist popularity will guide the recommendation of songs.

## Division of Labor:

- Jiayi Chen:
  1. Data Preprocessing: Cleansing and standardizing data for the recommendation engine.
  2. Algorithm Development: Implementing and tuning the collaborative and content-based filtering algorithms.

- Harper Qi:
  1. Rule-Based Logic Implementation: Developing the rule-based recommendation logic.
  2. Testing

## Explainability:
Adhering to the course requirement, this system will not only recommend songs but also provide reasons for each suggestion, such as shared attributes with liked songs or popularity among similar users.

## Technical Specifications:
The system will be developed in Python. We will also provide an annotated bibliography, including literature on recommendation system methodologies, their applications in music, and studies on user interaction with music platforms.
