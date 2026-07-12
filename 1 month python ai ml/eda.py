# # # EDA  = Exploratory Data Analysis
import matplotlib
matplotlib.use('Agg')  # Prevents Tkinter popup crashes by saving to a file instead

import matplotlib.pyplot as plt
import pandas as pd
import nltk

# Ensure tokenizers are downloaded
nltk.download('punkt')
nltk.download('punkt_tab')

# 1. Load the data properly
df = pd.read_csv("spam.csv", encoding="latin-1")

# 2. Slice out empty trailing columns
df = df.iloc[:, :2]

# 3. Rename columns properly
df.columns = ["target", "text"]

# 4. Clean spacing strings
df["target"] = df["target"].str.strip()

# 5. Extract Text Features (Character and word count)
df["num_characters"] = df["text"].apply(len)
df["num_words"] = df["text"].apply(lambda x: len(nltk.word_tokenize(x)))

# 6. Generate and save the Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(
    df["target"].value_counts(),
    labels=["Ham", "Spam"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#4CAF50", "#FF5722"],
)
plt.title("Distribution of Spam vs Ham Messages")

# Save chart directly to your folder since windows won't open it
plt.savefig("spam_distribution.png")
print("Success! Pie chart saved as 'spam_distribution.png'")
print(df[["target", "num_characters", "num_words"]].head())










# # NLTK  = Natural Language Toolkit

# import nltk
# nltk.download('punkt_tab')  # Download the necessary tokenizer models
# from nltk.tokenize import word_tokenize, sent_tokenize

# text  = "Hello, world! This is a test sentence. Let's see how it tokenizes."


# # Tokenize into sentences
# sentences = sent_tokenize(text)
# print("Sentences:", sentences)


# # Tokenize into words
# words = word_tokenize(text)
# print("Words:", words)






