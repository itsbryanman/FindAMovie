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
