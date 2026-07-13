# # # # EDA  = Exploratory Data Analysis
# import matplotlib
# matplotlib.use('Agg')  # Prevents Tkinter popup crashes by saving to a file instead

# import matplotlib.pyplot as plt
# import pandas as pd
# import nltk

# # Ensure tokenizers are downloaded
# nltk.download('punkt')
# nltk.download('punkt_tab')

# # 1. Load the data properly
# df = pd.read_csv("spam.csv", encoding="latin-1")

# # 2. Slice out empty trailing columns
# df = df.iloc[:, :2]

# # 3. Rename columns properly
# df.columns = ["target", "text"]

# # 4. Clean spacing strings
# df["target"] = df["target"].str.strip()

# # 5. Extract Text Features (Character and word count)
# df["num_characters"] = df["text"].apply(len)
# df["num_words"] = df["text"].apply(lambda x: len(nltk.word_tokenize(x)))

# # 6. Generate and save the Pie Chart
# plt.figure(figsize=(6, 6))
# plt.pie(
#     df["target"].value_counts(),
#     labels=["Ham", "Spam"],
#     autopct="%1.1f%%",
#     startangle=90,
#     colors=["#4CAF50", "#FF5722"],
# )
# plt.title("Distribution of Spam vs Ham Messages")

# # Save chart directly to your folder since windows won't open it
# plt.savefig("spam_distribution.png")
# print("Success! Pie chart saved as 'spam_distribution.png'")
# print(df[["target", "num_characters", "num_words"]].head())










# # # NLTK  = Natural Language Toolkit

# # import nltk
# # nltk.download('punkt_tab')  # Download the necessary tokenizer models
# # from nltk.tokenize import word_tokenize, sent_tokenize

# # text  = "Hello, world! This is a test sentence. Let's see how it tokenizes."


# # # Tokenize into sentences
# # sentences = sent_tokenize(text)
# # print("Sentences:", sentences)


# # # Tokenize into words
# # words = word_tokenize(text)
# # print("Words:", words)





# import matplotlib

# matplotlib.use("Agg")  # Prevents Tkinter popup crashes
# import matplotlib.pyplot as plt
# import nltk
# import pandas as pd
# import seaborn as sns

# # Ensure tokenizers are downloaded
# nltk.download("punkt")
# nltk.download("punkt_tab")

# # 1. Load the data properly
# df = pd.read_csv("spam.csv", encoding="latin-1")

# # 2. Slice out empty trailing columns
# df = df.iloc[:, :2]

# # 3. Rename columns properly
# df.columns = ["target", "text"]

# # 4. Clean spacing strings
# df["target"] = df["target"].str.strip()

# # 5. Convert target to numeric for heatmap correlation (Ham = 0, Spam = 1)
# df["target_numeric"] = df["target"].map({"ham": 0, "spam": 1})

# # 6. Extract Text Features using NLTK
# df["num_characters"] = df["text"].apply(len)
# df["num_words"] = df["text"].apply(lambda x: len(nltk.word_tokenize(x)))
# df["num_sentences"] = df["text"].apply(lambda x: len(nltk.sent_tokenize(x)))

# # 7. Calculate the correlation matrix
# # We only select the numeric columns for correlation
# numerical_df = df[
#     ["target_numeric", "num_characters", "num_words", "num_sentences"]
# ]
# correlation_matrix = numerical_df.corr()

# # 8. Generate and save the Heatmap
# plt.figure(figsize=(8, 6))
# sns.heatmap(
#     correlation_matrix,
#     annot=True,  # Shows the correlation numbers inside the squares
#     cmap="coolwarm",  # Red for positive correlation, blue for negative
#     vmin=-1,  # Minimum value for correlation scale
#     vmax=1,  # Maximum value for correlation scale
#     linewidths=0.5,
# )
# plt.title("Correlation Heatmap: Text Features vs Message Type")
# plt.tight_layout()

# # Save heatmap directly to your folder
# plt.savefig("spam_heatmap.png")
# print("Success! Heatmap saved as 'spam_heatmap.png'")
# print("\nCorrelation Matrix Values:")
# print(correlation_matrix)






# Data processing and feature extraction are crucial steps in preparing your dataset for machine learning models. In this code, we have performed the following steps: 


# ?sterps of data processing and feature extraction:
# lowercse 
# ?tokenization
# remove the special characters
# remove the stop words and punctuation


# def transform_text(text):
#     # Convert to lowercase
#     text = text.lower()

#     # Tokenize the text
#     tokens = nltk.word_tokenize(text)

#     # Remove special characters and punctuation
#     tokens = [word for word in tokens if word.isalnum()]

#     # Remove stop words
#     stop_words = set(nltk.corpus.stopwords.words("english"))

#     tokens = [word for word in tokens if word not in stop_words]
#     return " ".join(tokens)  
# 
# its more update version u can say



# import string
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
 
# # DOWNLOAD THE REQUIRED DATASETS ---
# nltk.download("punkt")
# nltk.download("punkt_tab")
# nltk.download("stopwords")
 
 
# # Initialize the stemmer
# ps = PorterStemmer()
 
 
# def transform_text(text):
#     # 1. Lowercase
#     text = text.lower()
 
#     # 2. Tokenize
#     tokens = nltk.word_tokenize(text)
 
#     # 3. Keep only alphanumeric tokens (removes punctuation)
#     tokens = [word for word in tokens if word.isalnum()]
 
#     # 4. Remove Stop Words
#     stop_words = set(stopwords.words("english"))
#     tokens = [word for word in tokens if word not in stop_words]
 
#     # 5. Apply Stemming
#     tokens = [ps.stem(word) for word in tokens]
 
#     # 6. Join back with space
#     return " ".join(tokens)
 
 
 
# print(transform_text("I loved the loving text messages you were sending!"))
 

import pandas as pd
import matplotlib.pyplot as plt


import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# DOWNLOAD THE REQUIRED DATASETS ---
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


# Initialize the stemmer
ps = PorterStemmer()


def transform_text(text):
    # 1. Lowercase
    text = text.lower()

    # 2. Tokenize
    tokens = nltk.word_tokenize(text)

    # 3. Keep only alphanumeric tokens (removes punctuation)
    tokens = [word for word in tokens if word.isalnum()]

    # 4. Remove Stop Words
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]

    # 5. Apply Stemming
    tokens = [ps.stem(word) for word in tokens]

    # 6. Join back with space
    return " ".join(tokens)



print(transform_text("I loved the loving text messages you were sending!"))


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


df["transformed_text"] = df["text"].apply(transform_text)
df.head()  # Display the first few rows of the DataFrame to verify the transformation

from wordcloud import WordCloud

wc = WordCloud(
    width=500, height=500, min_font_size=10, background_color="white"
)

# Generate the word cloud for spam messages
spam_wc = wc.generate(
    df[df["target"] == "spam"]["transformed_text"].str.cat(sep=" ")
)

# Plot and save the figure
plt.figure(figsize=(10, 8))
plt.imshow(spam_wc, interpolation="bilinear")
plt.axis("off")

# Save it to your folder
plt.savefig("spam_wordcloud.png")
print("Success! WordCloud saved as 'spam_wordcloud.png'")