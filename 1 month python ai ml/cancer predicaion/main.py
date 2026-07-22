# cancr predicitin

from pandas.core.tools.datetimes import Scalar
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
sns.heatmap(auto.corr(), annot=True, cmap="Blues")
plt.xticks(rotation=90)
plt.yticks(rotation=90)
plt.show()

# starting ann

yy = auto["TenYearCHD"]
XX = auto.drop("TenYearCHD", axis=1)

# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)

XX.shape()


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
XX = scaler.fit_transform(XX)
yy = scaler.fit_transform(yy.values.reshape(-1, 1))


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    XX, yy, test_size=0.2, random_state=42
)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
