import json
import requests

# Replace with your TMDb API key
TMDB_API_KEY = "1db1e7057b49dd2e81d9e188bd2edb54"

# Load watched movies from JSON file
def load_watched_movies(filename):
    with open(filename, 'r') as file:
        watched_movies = json.load(file)
    return watched_movies

# Analyze watched movies to extract preferences
def analyze_preferences(watched_movies):
    genres = {}
    total_rating = 0
    movie_count = 0
    years = []
    
    for movie in watched_movies:
        # Accumulate genre frequencies
        for genre in movie.get("genres", []):
            genres[genre] = genres.get(genre, 0) + 1
            
        # Add to rating and year lists for analysis
        total_rating += movie.get("rating", 0)
        years.append(movie.get("release_year", 0))
        movie_count += 1
    
    # Determine most common genres, average rating, and year range
    preferred_genres = sorted(genres, key=genres.get, reverse=True)[:2]
    avg_rating = total_rating / movie_count if movie_count else 7.0
    year_range = (min(years), max(years)) if years else (2000, 2024)
    
    return preferred_genres, avg_rating, year_range

# Fetch recommendations from TMDb based on preferences
def get_tmdb_recommendations(genre_ids, min_rating, release_year_range):
    url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "with_genres": ",".join(map(str, genre_ids)),
        "vote_average.gte": min_rating,
        "primary_release_date.gte": release_year_range[0],
        "primary_release_date.lte": release_year_range[1],
        "sort_by": "popularity.desc",
        "page": 1
    }
    response = requests.get(url, params=params)
    recommendations = response.json().get("results", [])
    return recommendations[:5]  # Top 5 results

# Map genre names to TMDb genre IDs
GENRE_MAP = {
    "Action": 28,
    "Adventure": 12,
    "Comedy": 35,
    "Drama": 18,
    "Fantasy": 14,
    "Horror": 27,
    "Science Fiction": 878,
    "Thriller": 53,
    # Add more as needed
}

# Main function to generate recommendations
def recommend_movies(filename):
    watched_movies = load_watched_movies(filename)
    preferred_genres, avg_rating, year_range = analyze_preferences(watched_movies)
    
    # Convert preferred genres to TMDb genre IDs
    genre_ids = [GENRE_MAP.get(genre) for genre in preferred_genres if genre in GENRE_MAP]
    
    # Fetch and display recommendations
    recommendations = get_tmdb_recommendations(genre_ids, avg_rating, year_range)
    print("Recommended Movies:")
    for movie in recommendations:
        print(f"Title: {movie['title']}, Rating: {movie['vote_average']}, Release Date: {movie['release_date']}")

# Run the recommendation function
recommend_movies("watched_movies.json")
