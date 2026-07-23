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
