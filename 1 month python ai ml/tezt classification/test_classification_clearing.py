"""
Text Classification Preprocessing Pipeline
=========================================
This script loads raw text data (BBC news dataset), performs exploratory data analysis (EDA),
cleans text using regular expressions, removes English stopwords, applies Porter Stemming,
and saves the cleaned dataset for downstream machine learning tasks.
"""

import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Ensure NLTK stopword corpus is downloaded silently
nltk.download('stopwords', quiet=True)

# ----------------------------------------------------
# 1. Text Preprocessing Function
# ----------------------------------------------------
def clean_text_pipeline(text: str, stemmer: PorterStemmer, stop_words: set) -> str:
    """
    Cleans a text string through the following pipeline:
    1. Removes all non-alphabetic characters (numbers, punctuation, symbols).
    2. Converts all text to lowercase.
    3. Tokenizes into words and removes standard English stopwords.
    4. Applies Porter Stemming to reduce words to their root forms.
    """
    if not isinstance(text, str):
        return ""

    # Step 1 & 2: Keep only alphabetic characters and convert to lower case
    text_alpha_only = re.sub(r"[^a-zA-Z]", " ", text).lower()

    # Step 3: Split into individual words
    words_in_text = text_alpha_only.split()

    # Step 4: Filter out stopwords and apply Porter Stemmer
    cleaned_words = [
        stemmer.stem(word) 
        for word in words_in_text 
        if word not in stop_words
    ]

    # Rejoin processed tokens into a single clean string
    return " ".join(cleaned_words)


# ----------------------------------------------------
# 2. Main Execution Flow
# ----------------------------------------------------
def main():
    # File Path Setup (Uses local file in current directory)
    file_path = "bbc-folderr.csv"
    if not os.path.exists(file_path):
        print(f"Error: Data file '{file_path}' not found in current directory.")
        return

    # --- Step 1: Data Loading & Shuffling ---
    print("Loading dataset...")
    df = pd.read_csv(file_path, encoding='latin1')
    
    # Drop rows with missing news text or categories
    df = df.dropna(subset=['news', 'category']).reset_index(drop=True)
    
    # Shuffle dataset randomly
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # --- Step 2: Exploratory Data Analysis (EDA) ---
    print("\n--- Exploratory Data Analysis ---")
    print(f"Total dataset records: {len(df)}")
    print(f"Unique news categories found: {set(df['category'])}")
    
    print("\nCategory Distribution:")
    category_counts = df.groupby('category')['category'].count()
    print(category_counts)

    # Sample check of original news article length (in words)
    first_news_sample = df['news'].iloc[0]
    sample_word_count = len(first_news_sample.split())
    print(f"\nSample article word count: {sample_word_count} words")

    # Plot Category Counts
    category_counts.plot.bar(color='skyblue', edgecolor='black')
    plt.title("BBC News Categories Distribution")
    plt.xlabel("Category")
    plt.ylabel("Article Count")
    plt.tight_layout()
    print("\nDisplaying category distribution bar chart...")
    plt.show()

    # --- Step 3: Text Preprocessing & Cleaning ---
    print("\nStarting text cleaning pipeline...")
    stemmer = PorterStemmer()
    english_stopwords = set(stopwords.words("english"))

    # Apply preprocessing to all news articles
    df['cleaned'] = df['news'].apply(
        lambda text: clean_text_pipeline(text, stemmer, english_stopwords)
    )

    # Inspect sample before and after cleaning
    print("\n--- Preprocessing Demonstration ---")
    print("Original Text Sample (first 150 chars):")
    print(first_news_sample[:150], "...")
    print("\nCleaned & Stemmed Text Sample (first 150 chars):")
    print(df['cleaned'].iloc[0][:150], "...")

    # --- Step 4: Export Processed Dataset ---
    output_file = "cleaned_news_data.csv"
    output_cols = ['category', 'news', 'cleaned']
    
    df[output_cols].to_csv(output_file, index=False)
    print(f"\nCleaned dataset saved successfully to: '{output_file}'")

if __name__ == "__main__":
    main()