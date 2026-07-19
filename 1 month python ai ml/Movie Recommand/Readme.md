# 🎬 Movie Recommendation System (Content-Based Filtering)

## 📌 Project Overview

This project is a **Content-Based Movie Recommendation System** built using **Python**, **Pandas**, and **Scikit-learn**.

The system recommends movies based on their **genre** and **overview (story description)**.

Instead of using user ratings or watch history, it compares the content of movies to find similar ones.

---

# 📂 Dataset

The dataset contains the following columns:

| Column            | Description             |
| ----------------- | ----------------------- |
| id                | Unique Movie ID         |
| title             | Movie Name              |
| genre             | Movie Genres            |
| original_language | Original Language       |
| overview          | Movie Story Description |
| popularity        | Popularity Score        |
| release_date      | Release Date            |
| vote_average      | Average Rating          |
| vote_count        | Number of Votes         |

Example:

| id  | title                    | genre        | overview               |
| --- | ------------------------ | ------------ | ---------------------- |
| 278 | The Shawshank Redemption | Drama, Crime | Framed in the 1940s... |

---

# 🧠 Recommendation Method

This project uses **Content-Based Filtering**.

Instead of asking:

> "What movies did other users like?"

it asks:

> "Which movies have similar content?"

Movies are compared using:

- Genre
- Overview (Story Description)

---

# 🚀 Project Workflow

```
Load Dataset
      │
      ▼
Select Useful Columns
      │
      ▼
Remove Missing Data
      │
      ▼
Create Tags
      │
      ▼
Convert Text to Numbers
      │
      ▼
Calculate Cosine Similarity
      │
      ▼
User Searches Movie
      │
      ▼
Find Similar Movies
```

---

# Step 1 — Import Libraries

Libraries used:

- pandas
- CountVectorizer
- cosine_similarity

Purpose:

- Read the dataset.
- Convert text into vectors.
- Compare movies mathematically.

---

# Step 2 — Load the Dataset

```python
movies = pd.read_csv("dataset.csv")
```

Purpose:

Read the CSV file into a Pandas DataFrame.

---

# Step 3 — Explore the Dataset

Check:

- First few rows
- Column names
- Missing values
- Duplicate rows
- Dataset size

Commands:

```python
movies.head()

movies.info()

movies.isnull().sum()

movies.duplicated().sum()

movies.shape
```

Purpose:

Understand the data before processing it.

---

# Step 4 — Select Useful Columns

Keep only:

- id
- title
- overview
- genre

```python
movies = movies[
[
"id",
"title",
"overview",
"genre"
]
]
```

Purpose:

Remove unnecessary columns that are not useful for recommendations.

---

# Step 5 — Handle Missing Values

```python
movies.dropna(inplace=True)
```

Purpose:

Some movies may not have an overview or genre.

Removing them prevents errors later.

---

# Step 6 — Create Tags

Combine:

Overview

-

Genre

```python
movies["tags"] = movies["overview"] + " " + movies["genre"]
```

Example:

Overview

```
A prisoner escapes from jail.
```

Genre

```
Drama Crime
```

Tags

```
A prisoner escapes from jail Drama Crime
```

Purpose:

Store all important information in one text column.

---

# Step 7 — Remove Old Columns

```python
new_data = movies.drop(columns=["overview","genre"])
```

Purpose:

Since the information already exists inside Tags, the original columns are no longer needed.

---

# Step 8 — Convert Text to Lowercase

```python
new_data["tags"] = new_data["tags"].str.lower()
```

Purpose:

Treat:

Drama

and

drama

as the same word.

---

# Step 9 — Convert Text into Numbers

Computers cannot perform mathematical operations on text.

Example:

```
hero fights alien
```

becomes

```
[1 1 1 0 0 ...]
```

using CountVectorizer.

```python
cv = CountVectorizer(
max_features=10000,
stop_words="english"
)

vectors = cv.fit_transform(
new_data["tags"]
).toarray()
```

Purpose:

Convert text into numerical vectors.

---

# Step 10 — Calculate Cosine Similarity

```python
similarity = cosine_similarity(vectors)
```

Purpose:

Compare every movie with every other movie.

Output:

```
Movie A ↔ Movie B = 0.91

Movie A ↔ Movie C = 0.22
```

Higher score means the movies are more similar.

---

# Step 11 — User Searches a Movie

Example:

```
Avatar
```

Find its row index.

```python
index = new_data[
new_data["title"]=="Avatar"
].index[0]
```

Purpose:

Locate the selected movie inside the dataset.

---

# Step 12 — Get Similarity Scores

```python
similarity[index]
```

Purpose:

Retrieve similarity scores between the selected movie and every other movie.

---

# Step 13 — Use enumerate()

```python
enumerate(similarity[index])
```

Output:

```
(0,1.0)

(1,0.83)

(2,0.71)

(3,0.45)
```

Purpose:

Attach each similarity score to its corresponding movie index.

---

# Step 14 — Sort Movies

```python
sorted(
enumerate(similarity[index]),
reverse=True,
key=lambda x:x[1]
)
```

Purpose:

Sort movies from most similar to least similar.

---

# Step 15 — Recommend Movies

Skip the first movie because it is the searched movie itself.

Display the next five highest similarity scores.

Example:

```
Input:

Avatar

Recommendations:

Avatar: The Way of Water

Guardians of the Galaxy

John Carter

Star Trek

The Fifth Element
```

---

# 📚 Machine Learning Concepts Used

### Content-Based Filtering

Recommend movies using movie information instead of user ratings.

---

### Feature Engineering

Creating the **Tags** column by combining:

- Overview
- Genre

---

### Bag of Words (BoW)

CountVectorizer converts text into vectors.

---

### CountVectorizer

Converts words into numerical features.

---

### Vector

A numerical representation of text.

Example:

```
hero alien war
↓

[1,1,1,0,0]
```

---

### Cosine Similarity

Measures similarity between two vectors.

Range:

```
1.0 → Exactly the same

0.0 → Completely different
```

---

# 📦 Libraries Used

- Python
- Pandas
- Scikit-learn

---

# 💡 Future Improvements

- Add stemming using PorterStemmer
- Save the model using Pickle
- Build a Streamlit web application
- Recommend movies using posters
- Search movies without case sensitivity
- Use TF-IDF instead of CountVectorizer
- Add fuzzy matching for misspelled movie names
- Combine content-based and collaborative filtering

---

# 📌 Final Pipeline

```
Dataset
    │
    ▼
Select Columns
    │
    ▼
Remove Missing Data
    │
    ▼
Create Tags
    │
    ▼
Text Preprocessing
    │
    ▼
CountVectorizer
    │
    ▼
Movie Vectors
    │
    ▼
Cosine Similarity
    │
    ▼
User Input
    │
    ▼
Find Movie
    │
    ▼
Sort Similarity Scores
    │
    ▼
Top 5 Recommendations
```

---

# ✅ Skills Learned

- Data Cleaning
- Feature Engineering
- Natural Language Processing (NLP)
- Bag of Words
- CountVectorizer
- Cosine Similarity
- Content-Based Recommendation Systems
- Pandas Data Processing
- Machine Learning Pipeline
