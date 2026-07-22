# cancr predicitin

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import xticks, yticks
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


#  data cleaning and proccessing


# load dataset
df = pd.read_csv("breast_cancer.csv")
print(df.head())


print(df.shape)

print(df.describe())

print(df.info())

print(df.columns)


# checking null

df.isnull()

df = df.dropna()


auto = df


# starting the machine learning

plt.figure(figsize=(10, 10))
sns.heatmap(auto.corr(), annot=True, cmap="coolwarm")
plt.xticks(rotation=90)
plt.yticks(rotation=90)
plt.show()
