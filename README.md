# Content-Based Movie Recommender System

## Overview

This project is a content-based movie recommender system designed to suggest movies to users based on the content of the movies they have liked. The recommendation system leverages textual data preprocessing and machine learning techniques to provide accurate and relevant movie recommendations.

## Features

- **Textual Data Preprocessing**: Utilizes `NLTK` and `scikit-learn` for efficient textual data preprocessing.
- **Feature Extraction**: Employs `TF-IDF Vectorizer` to convert text data into numerical features.
- **Similarity Calculation**: Uses `cosine similarity` to find and recommend movies that are similar to the user's preferences.
- **Interactive UI**: Deployed using `Streamlit` to provide an intuitive and interactive user interface for users to receive movie recommendations.
- **Version Control**: Managed through `Git` to ensure consistent and trackable project development.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/IshaanMehta/Movie-Recommendation-System.git
    cd Movie-Recommendation-System
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the project root directory and add your API key:
    ```
    API_KEY="your-api-key"
    ```

5. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Dataset

The dataset used for this project contains various features related to movies such as `budget`, `genres`, `homepage`, `original_language`, `title`, `overview`, `popularity`, `release_date`, `revenue`, `runtime`, `vote_average`, `vote_count`, `cast`, and `crew`.

You can download the dataset from the following link:
[TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Project Structure

- `app.py`: Main file to run the Streamlit app.
- `data_processing.py`: Module for loading and preprocessing the dataset.
- `recommender.py`: Module containing the recommendation logic.
- `movie_posters.py`: Module to fetch movie posters from an external API.
- `Movie_Recommender.ipynb`: Jupyter Notebook with data cleaning, preprocessing, analysis, and recommender creation.
- `requirements.txt`: File listing all the dependencies required to run the project.

## Usage

1. Start the Streamlit application.
2. Select a movie title from the dropdown.
3. Click on the "Recommendation" button to get a list of recommended movies along with their posters.

## Jupyter Notebook

The `Movie_Recommender.ipynb` file contains the complete process of data cleaning, preprocessing, analysis, and the creation of the recommender system. This notebook provides detailed insights and steps involved in building the recommender.

## Libraries and Tools

- `NLTK`
- `scikit-learn`
- `Streamlit`
- `pandas`
- `numpy`
- `requests`
- `Git`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
