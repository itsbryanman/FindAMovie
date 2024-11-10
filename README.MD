# Movie Recommendations from Watched List

This project analyzes a JSON file of watched movies to generate personalized movie recommendations. By extracting patterns in your movie preferences—such as genre, average rating, and release year—the program uses The Movie Database (TMDb) API to suggest 5 new movies you may enjoy.

## Features

- **Genre Preference Analysis**: Determines your favorite genres from the movies you've watched.
- **Average Rating Filtering**: Suggests movies close to your typical rating.
- **Year Range Customization**: Recommends movies from your preferred release years.
- **Easy TMDb Integration**: Utilizes TMDb's movie discover features for accurate recommendations.

## Requirements

- **Python 3.x**
- **Requests Library**: Install using `pip install requests`
- **TMDb API Key**: Sign up at [The Movie Database](https://www.themoviedb.org/) to get your API key.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommendations.git



Instructions for FindAMovie.py
FindAMovie.py is a Python script that analyzes a JSON file of watched movies and provides personalized movie recommendations using The Movie Database (TMDb) API.

1. Prerequisites
Python 3.x: Make sure Python is installed. You can download it from Python's website.
API Key for TMDb: Sign up at The Movie Database and get an API key to access the movie data.
2. Dependencies
Install the requests library to make API calls to TMDb:

bash
Copy code
pip install requests
3. File Setup
Download FindAMovie.py: Save the script in a folder on your computer.

Create your JSON file: Place a JSON file named watched_movies.json in the same directory as FindAMovie.py. This file should contain information about movies you've watched in the following format:

json
Copy code
[
    {
        "title": "Inception",
        "genres": ["Action", "Science Fiction"],
        "rating": 8.8,
        "release_year": 2010
    },
    {
        "title": "The Dark Knight",
        "genres": ["Action", "Drama"],
        "rating": 9.0,
        "release_year": 2008
    }
    // More movies
]
Update the API Key:

Open FindAMovie.py in a text editor.
Replace YOUR_TMDB_API_KEY with your actual TMDb API key in the line:
python
Copy code
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
4. Running the Script
In your terminal, navigate to the directory where FindAMovie.py and watched_movies.json are located, and run:

bash
Copy code
python FindAMovie.py
5. Understanding the Output
The script will analyze your JSON file to find patterns in your movie-watching history and will print 5 new movie recommendations to the terminal based on your preferred genres, rating, and release years.

The output will look like this:

plaintext
Copy code
Recommended Movies:
Title: Edge of Tomorrow, Rating: 7.9, Release Date: 2014-06-06
Title: Interstellar, Rating: 8.6, Release Date: 2014-11-05
Title: Mad Max: Fury Road, Rating: 8.1, Release Date: 2015-05-15
Title: The Martian, Rating: 8.0, Release Date: 2015-10-02
Title: Guardians of the Galaxy, Rating: 7.9, Release Date: 2014-08-01
6. Customizing Recommendations
Genres: Modify the genres in your watched_movies.json file to influence genre preferences.
Rating Range: Adjust the ratings in watched_movies.json if you want different average ratings.
Release Years: Use specific release years in watched_movies.json to refine the range of release years in recommendations.
