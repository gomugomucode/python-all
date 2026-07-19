# # movie recommandation system

# import pandas as pd

# movie_data = pd.read_csv("dataset.csv")

# # print(movie_data.head(10))

# # print(movie_data.info())

# movie_data = movie_data.columns[
#     [
#         "id",
#         "title",
#         "genre",
#         "original_language",
#         "overview",
#         "popularity",
#         "release_date",
#         "vote_average",
#         "vote_count",
#     ]
# ]


# movie_data = movie_data[["id", "title", "genre", "overview"]]

# print(movie_data.head())

# movie_data.isnull().sum()
# movie_data = movie_data.dropna()


# print(movie_data.shape)

# movie_data.duplicated().sum()


# Movie Recommendation System

import pandas as pd

movies = pd.read_csv("dataset.csv")
print("movies")
print(movies.head(10))
print("movies.info")

print("movies.isnull().sum")

print("movies.shape")

print("movies.duplicated().sum")

print("movies.columns")

movies = movies[["id", "title", "overview", "genre"]]
print(movies.head(10))
movies["tags"] = movies["overview"] + movies["genre"]
print("movies")
new_data = movies.drop(columns=["overview", "genre"])
print("new_data")

print(new_data)
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=10000, stop_words="english")
vector = cv.fit_transform(new_data["tags"].values.astype("U")).toarray()
vector.shape


from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vector)
print("similarity")

print(new_data[new_data["title"] == "Avatar"].index[0])

distance = sorted(enumerate(similarity[0]), reverse=True, key=lambda x: x[1])

print(distance)
print(distance[1])
