# 🎬 Movie Recommendations from Watched List

This project analyzes a JSON file of your watched movies and generates personalized movie recommendations. By identifying patterns in your viewing preferences—such as genres, average ratings, and release years—the program uses The Movie Database (TMDb) API to suggest 5 new movies you might enjoy.

---

## 🚀 Features

- **Genre Analysis**: Finds your favorite genres from previously watched movies.
- **Rating-Based Suggestions**: Recommends movies close to your preferred rating range.
- **Release Year Customization**: Suggests movies from your favorite release periods.
- **Seamless TMDb Integration**: Leverages TMDb's movie discover features for precise recommendations.

---

## 📋 Requirements

- **Python 3.x**
- **Requests Library**: Install it via `pip install requests`
- **TMDb API Key**: Sign up at [The Movie Database](https://www.themoviedb.org/) to get your free API key.

---

## ⚙️ Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendations.git
```

### Step 2: Install Dependencies

Use the following command to install the `requests` library for making API calls to TMDb:

```bash
pip install requests
```

### Step 3: File Setup

1. **Download `FindAMovie.py`**: Save the script in a folder on your computer.
2. **Create Your JSON File**: Place a JSON file named `watched_movies.json` in the same directory as `FindAMovie.py`. Use this format for each movie you've watched:

    ```json
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
        // Add more movies here
    ]
    ```

3. **Update the API Key**:  
   - Open `FindAMovie.py` in a text editor.
   - Replace `YOUR_TMDB_API_KEY` with your TMDb API key on the line:

     ```python
     TMDB_API_KEY = "YOUR_TMDB_API_KEY"
     ```

---

## ▶️ Running the Script

Navigate to the directory where `FindAMovie.py` and `watched_movies.json` are located and execute the following command:

```bash
python FindAMovie.py
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
