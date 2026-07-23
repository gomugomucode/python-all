# # text classification clearning
# import numpy as np
# import pandas as pd
# import re, string
# import matplotlib.pyplot as plt
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import classification_report, confusion_matrix
# from sklearn.model_selection import train_test_split
# from sklearn.feature_selection import SelectKBest, chi2
# import pickle
# import nltk

# nltk.download('stopwords')
# %matplotlib inline

# df = pd.read_csv('/content/bbc-folder - bbc-folder.csv', encoding = 'latin1')
# df = df.sample(frac = 1)
# df

# len(df['news'][0].split())


# #No of a categories
# set(df['category'])


import numpy as np
import pandas as pd
import re,string
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
import pickle
import nltk
nltk.download('stopwords')
%matplotlib inline

df = pd.read_csv('/content/bbc-folder - bbc-folder.csv', encoding = 'latin1')
df = df.sample(frac = 1)
df
len(df['news'][0].split())
#No of a categories
set(df['category'])
df.groupby('category').category.count()
#Analyzing data
df.groupby('category').category.count().plot.bar()
plt.show()
# Data Cleaning using regex
regs = re.sub("[^a-zA-Z]", " ", df['news'][0]).lower()
regs
#stop words
nltk.download('stopwords')
words = stopwords.words("english")
print(words)
print(len(words))
# Data Cleaning using stemmer

stemmer = PorterStemmer()
data = "I am loving computing I have a computer".split()
" ".join([stemmer.stem(i) for i in data])
# stemmer.stem("")
# print(words)
# news = df['text'][0].split()
# for i in words:
#   c = news.count(i)
#   for j in range(c):
#     news.remove(i)

# print(" ".join(news))
regs.lower().split()
' '.join([i for i in regs.lower().split() if i not in words])
# Data Cleaning removing stopwords
words = stopwords.words("english")
without_stop_words_of_a_news = " ".join([i for i in regs.lower().split() if i not in words])
without_stop_words_of_a_news
df = df.dropna()
# Doing all cleaning process using regex, stemmer, stopwords for all data
def clean_text_pipeline(text):
    # Apply regex cleaning and convert to lowercase
    text = re.sub("[^a-zA-Z]", " ", text).lower()
    # Split into words
    words_in_text = text.split()
    # Remove stopwords (using 'words' list defined earlier)
    words_without_stopwords = [word for word in words_in_text if word not in words]
    # Apply stemming (using 'stemmer' object defined earlier)
    stemmed_words = [stemmer.stem(word) for word in words_without_stopwords]
    return " ".join(stemmed_words)

df['cleaned'] = df['news'].apply(clean_text_pipeline)
df
# " ".join([stemmer.stem(i) for i in without_stop_words_of_a_news.lower().split()])
# list(filter(lambda x: [stemmer.stem(i) for i in re.sub("[^a-zA-Z]", " ", x).split() if i not in words],df['text']))
# #cleaning dataset
# nltk.download('stopwords')
# stemmer = PorterStemmer()
# words = stopwords.words("english")
# words.extend(['a','an','the'])
# df['cleaned'] = df['cleaned'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z]", " ", x.lower()).split() if i not in words]).lower())
# # df['newcleaned'] = [(i for i in list(df['cleaned'])).split() if i not in words ]
# df
df.to_csv('cleaned_news.csv')
# df['cleaned'] = df['text'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z]", " ", x).split() ]).lower())
# df
# print(words)
# words = stopwords.words("nepali")
# words
df['cleaned'] = df['news'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z]", " ", x).split() if i not in words]).lower())
df
df1 = df[['news','cleaned']]
df1.to_csv('cleaned_news_data')
len(df['cleaned'][0])