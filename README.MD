# 🎬 Movie Recommendations from Watched List

This project analyzes a JSON file of your watched movies and generates personalized movie recommendations. It automatically retrieves genre information from TMDb and selects films similar to your viewing habits. The script outputs five suggestions based on genre frequency, average ratings and release periods.

---

## 🚀 Features

- **Genre Analysis**: Finds your favorite genres from previously watched movies.
- **Rating-Based Suggestions**: Recommends movies close to your preferred rating range.
- **Release Year Customization**: Suggests movies from your favorite release periods.
- **Seamless TMDb Integration**: Leverages TMDb's movie discover features for precise recommendations.

---

## 📋 Requirements

- **Python 3.8+**
- **TMDb API Key**: sign up at [The Movie Database](https://www.themoviedb.org/) for a free key.

---

## ⚙️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/movie-recommendations.git
   cd movie-recommendations
   ```

2. **Create a virtual environment and install dependencies**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set your TMDb API key**

   Obtain an API key from TMDb and set it in your environment:

   ```bash
   export TMDB_API_KEY="<your api key>"
   ```

4. **Prepare your watch list**

   Create a JSON file named `watched_movies.json` in the project directory. Each entry should contain a title, a list of genres, a numeric rating and the release year.

---

## ▶️ Running the Script

Execute the program with the path to your watch list:

```bash
python FindAMovie.py watched_movies.json
```

---

## 📊 Understanding the Output

The script will analyze your JSON file for patterns in genre, rating, and release year. It will then print 5 new movie recommendations based on your viewing habits:

Example Output:
```plaintext
Recommended Movies:
Title: Edge of Tomorrow, Rating: 7.9, Release Date: 2014-06-06
Title: Interstellar, Rating: 8.6, Release Date: 2014-11-05
Title: Mad Max: Fury Road, Rating: 8.1, Release Date: 2015-05-15
Title: The Martian, Rating: 8.0, Release Date: 2015-10-02
Title: Guardians of the Galaxy, Rating: 7.9, Release Date: 2014-08-01
```

---

## 🎛 Customizing Your Recommendations

You can tailor the recommendations further by modifying the information in your JSON file:

- **Genres**: Adjust the genres to influence genre-based recommendations.
- **Ratings**: Change ratings to adjust the target rating range.
- **Release Years**: Use specific release years to fine-tune recommendations to your favorite eras.

---

YOU CAN IMPORT YOUR TRAKT.TV JSON LISTS, USE TRACT BACKUP https://darekkay.com/blog/trakt-tv-backup/
