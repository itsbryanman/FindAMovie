"""Find and recommend movies based on a user's viewing history."""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

import requests


@dataclass
class WatchedMovie:
    title: str
    genres: List[str]
    rating: float
    release_year: int


TMDB_API_KEY_ENV = "TMDB_API_KEY"
TMDB_BASE_URL = "https://api.themoviedb.org/3"


class TMDBClient:
    """Client for interacting with The Movie Database API."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def _get(self, endpoint: str, **params) -> dict:
        params["api_key"] = self.api_key
        response = requests.get(f"{TMDB_BASE_URL}{endpoint}", params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def fetch_genre_map(self) -> Dict[str, int]:
        genres = self._get("/genre/movie/list").get("genres", [])
        return {genre["name"]: genre["id"] for genre in genres}

    def discover_movies(
        self,
        *,
        genre_ids: Iterable[int],
        min_rating: float,
        release_year_range: Tuple[int, int],
    ) -> List[dict]:
        params = {
            "with_genres": ",".join(map(str, genre_ids)),
            "vote_average.gte": min_rating,
            "primary_release_date.gte": release_year_range[0],
            "primary_release_date.lte": release_year_range[1],
            "sort_by": "popularity.desc",
            "page": 1,
        }
        data = self._get("/discover/movie", **params)
        return data.get("results", [])[:5]


def load_watched_movies(path: str) -> List[WatchedMovie]:
    with open(path, "r", encoding="utf-8") as fh:
        raw_movies = json.load(fh)
    movies: List[WatchedMovie] = []
    for movie in raw_movies:
        movies.append(
            WatchedMovie(
                title=movie.get("title", ""),
                genres=movie.get("genres", []),
                rating=float(movie.get("rating", 0)),
                release_year=int(movie.get("release_year", 0)),
            )
        )
    return movies


def analyze_preferences(movies: Iterable[WatchedMovie]) -> Tuple[List[str], float, Tuple[int, int]]:
    genre_frequency: Dict[str, int] = {}
    total_rating = 0.0
    years: List[int] = []

    for m in movies:
        for g in m.genres:
            genre_frequency[g] = genre_frequency.get(g, 0) + 1
        total_rating += m.rating
        years.append(m.release_year)

    preferred_genres = sorted(genre_frequency, key=genre_frequency.get, reverse=True)[:2]
    avg_rating = total_rating / len(list(movies)) if movies else 7.0
    year_range = (min(years), max(years)) if years else (2000, 2024)
    return preferred_genres, avg_rating, year_range


def recommend_movies(json_file: str, api_key: str) -> None:
    movies = load_watched_movies(json_file)
    preferred_genres, avg_rating, year_range = analyze_preferences(movies)
    client = TMDBClient(api_key)
    genre_map = client.fetch_genre_map()
    genre_ids = [genre_map[g] for g in preferred_genres if g in genre_map]
    recommendations = client.discover_movies(
        genre_ids=genre_ids,
        min_rating=avg_rating,
        release_year_range=year_range,
    )
    print("Recommended Movies:")
    for movie in recommendations:
        print(f"{movie['title']} (Rating: {movie['vote_average']}, Release: {movie['release_date']})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", help="Path to watched_movies.json")
    args = parser.parse_args()

    api_key = os.getenv(TMDB_API_KEY_ENV)
    if not api_key:
        raise RuntimeError(f"{TMDB_API_KEY_ENV} environment variable not set")

    recommend_movies(args.json_file, api_key)


if __name__ == "__main__":
    main()
