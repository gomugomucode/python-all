# =====================================================
# Movie Recommendation System (Content-Based Filtering)
# =====================================================

# -----------------------------------------------------
# STEP 1: Import the required libraries
# -----------------------------------------------------

import pandas as pd

# CountVectorizer converts text into numbers
from sklearn.feature_extraction.text import CountVectorizer

# Cosine Similarity compares two vectors
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------------------------------
# STEP 2: Load the dataset
# -----------------------------------------------------

movies = pd.read_csv("dataset.csv")

print("Dataset Loaded Successfully!\n")

# Display first 5 rows
print(movies.head())


# -----------------------------------------------------
# STEP 3: Check the dataset
# -----------------------------------------------------

print("\nInformation about Dataset")
movies.info()

print("\nMissing Values")
print(movies.isnull().sum())

print("\nDataset Shape")
print(movies.shape)

print("\nDuplicate Rows")
print(movies.duplicated().sum())

print("\nColumn Names")
print(movies.columns)


# -----------------------------------------------------
# STEP 4: Keep only the useful columns
# -----------------------------------------------------
# We only need:
# id -> movie id
# title -> movie name
# overview -> story
# genre -> movie category

movies = movies[["id", "title", "overview", "genre"]]

print("\nUseful Columns")
print(movies.head())


# -----------------------------------------------------
# STEP 5: Remove missing values
# -----------------------------------------------------

movies = movies.dropna()


# -----------------------------------------------------
# STEP 6: Create a new feature called Tags
# -----------------------------------------------------
# We combine the overview and genre.
#
# Example:
#
# Overview:
# "A prisoner escapes from jail"
#
# Genre:
# "Drama Crime"
#
# Tags:
# "A prisoner escapes from jail Drama Crime"

movies["tags"] = movies["overview"] + " " + movies["genre"]


# -----------------------------------------------------
# STEP 7: Remove overview and genre
# -----------------------------------------------------
# Because the information is already stored inside Tags.

new_data = movies.drop(columns=["overview", "genre"])

print("\nNew Dataset")
print(new_data.head())


# -----------------------------------------------------
# STEP 8: Convert text into lowercase
# -----------------------------------------------------
# This keeps "Drama" and "drama" the same.

new_data["tags"] = new_data["tags"].str.lower()


# -----------------------------------------------------
# STEP 9: Convert text into vectors
# -----------------------------------------------------
#
# Computers cannot understand text.
#
# CountVectorizer converts every movie into numbers.
#
# Example:
#
# hero fights alien
#
# becomes
#
# [1 1 1 0 0 0 ...]

cv = CountVectorizer(max_features=10000, stop_words="english")

vectors = cv.fit_transform(new_data["tags"].values.astype("U")).toarray()

print("\nVector Shape")
print(vectors.shape)


# -----------------------------------------------------
# STEP 10: Calculate similarity between every movie
# -----------------------------------------------------
#
# Cosine similarity returns a matrix.
#
# similarity[i][j]
#
# tells how similar movie i is to movie j.

similarity = cosine_similarity(vectors)

print("\nSimilarity Matrix Shape")
print(similarity.shape)


# -----------------------------------------------------
# STEP 11: Create Recommendation Function
# -----------------------------------------------------


def recommend(movie_name):

    # Find the index of the movie entered by the user
    movie_index = new_data[new_data["title"] == movie_name].index[0]

    # Get similarity scores of that movie
    distances = similarity[movie_index]

    # Add index with similarity score
    movie_list = list(enumerate(distances))

    # Sort from highest similarity to lowest
    movie_list = sorted(movie_list, reverse=True, key=lambda x: x[1])

    print("\nRecommended Movies\n")

    # Skip first movie because it is the same movie
    for movie in movie_list[1:6]:

        print(new_data.iloc[movie[0]].title, " --> Similarity:", round(movie[1], 3))


# -----------------------------------------------------
# STEP 12: Take movie name from the user
# -----------------------------------------------------

movie = input("\nEnter Movie Name: ")

recommend(movie)
